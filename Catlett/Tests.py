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
import plotly.graph_objects as go

pathname = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/'
datafile = 'Reduced_GS.csv'

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
'''
na_indx = np.where((data['longitude']<(-50)) & (data['latitude']>0))
new_data = data.loc[(data['longitude']<(-50)) & (data['latitude']>0)]
new_data = new_data.loc[:, ~data.columns.str.contains('^Unnamed')]
#new_data = new_data.drop['Unnamed: 0',axis = 1]
new_data.to_csv(pathname + 'North_America_Only.csv')
#long_indx = np.where(data['longitude']>0)
latitude = data['latitude'].values
longitude = data['longitude'].values
#lat,long = np.meshgrid(latitude,longitude)
fig = plt.figure()
#plt.scatter(longitude[long_indx],latitude[lat_indx])
plt.plot(locs[0],locs[1],'.k')
plt.scatter(new_data['longitude'],new_data['latitude'],color='r')