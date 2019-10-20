#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 03:38:41 2019

@author: victoriacatlett
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shapefile
path = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/'

shpFilePath = "/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/states_21basic/states.shp"  
locs=[[],[]]
#listy=[]
test = shapefile.Reader(shpFilePath)
for sr in test.shapeRecords():
    for xNew,yNew in sr.shape.points:
        locs[0].append(xNew)
        locs[1].append(yNew)


yelp_data = pd.read_csv(path + 'yelp_data.csv')
bigf = pd.read_csv(path + 'template_data_fully_filled.csv')

y_lat = yelp_data['y_lat'].values
y_long = yelp_data['y_long'].values
y_zip = yelp_data['y_zip'].values
y_name = yelp_data['name'].values
y_address = yelp_data['address'].values

big_lat = bigf['latitude'].values
big_long = bigf['longitude'].values
big_zip = bigf['postalCode'].values
big_name = bigf['name'].values
big_address = bigf['address'].values
#print(yelp_data['name'])
'''
for i in range(55596):
    indx = np.where((y_address[i]==big_address))

    
    print(indx)
'''
plt.plot(locs[0],locs[1],'.k')
plt.scatter(big_long, big_lat, color = 'b', label = 'GS Data')
plt.scatter(y_long,y_lat, color = 'r', label = 'Yelp Data')
plt.legend()
plt.xlabel('Longitude (degrees)')
plt.ylabel('Latitude (degrees)')