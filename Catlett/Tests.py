#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:49:14 2019

@author: victoriacatlett
"""

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import mpl_toolkits
#from mpl_toolkits.basemap import Basemap
import pandas as pd
import shapefile
import seaborn as sns
import json
pathname = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/'
datafile = 'template_data_filled.csv'

data = pd.read_csv(pathname + datafile)
shpFilePath = "/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/states_21basic/states.shp"  
locs=[[],[]]
#listy=[]
test = shapefile.Reader(shpFilePath)
for sr in test.shapeRecords():
    for xNew,yNew in sr.shape.points:
        locs[0].append(xNew)
        locs[1].append(yNew)

'''
null_data = data.loc[:, data.columns.str.contains('^Unnamed')]
null_counts = sum(null_data.count())
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
print(data.columns)
data.to_csv(pathname + 'Reduced_GS.csv')

na_indx = np.where((data['longitude']<(-50)) & (data['latitude']>0))
new_data = data.loc[(data['longitude']<(-50)) & (data['latitude']>0)]
new_data = new_data.loc[:, ~data.columns.str.contains('^Unnamed')]
#new_data = new_data.drop['Unnamed: 0',axis = 1]
new_data.to_csv(pathname + 'North_America_Only.csv')
#long_indx = np.where(data['longitude']>0)
'''

latitude = data['latitude'].values
longitude = data['longitude'].values
types = data['Item_Type'].values
#lat,long = np.meshgrid(latitude,longitude)
fig = plt.figure()
plt.plot(locs[0],locs[1],'.k')
colors = ['r','darkorange','gold','limegreen','darkgreen','cyan','b','purple','grey','k']

sns.scatterplot(longitude,latitude, hue = types, palette = colors)
plt.xlabel('Longitude (degrees)')
plt.ylabel('Latitude (degrees)')