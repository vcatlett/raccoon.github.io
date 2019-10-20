#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:08:08 2019

@author: victoriacatlett
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.constants as c

my_lat = 33
my_long = -96
my_rad = 100

pathname = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/'
datafile = 'North_America_Only.csv'
data = pd.read_csv(pathname + datafile)

lats = data['latitude'].values
longs = data['longitude'].values
restaurants = data['name'].values

c_earth = 24901.

def find_tacos(lat, long, rad):
    res_theta = (rad/c_earth)*360.
    
    indx = np.where((np.square(lats-lat)+np.square(longs-long)) <= (res_theta**2))
    
    res_lat = lats[indx]
    res_long = longs[indx]
    
    fig, ax = plt.subplots(1)
    plt.plot(long, lat, 'or')
    circle1 = plt.Circle((long, lat), radius = res_theta, ec = 'r', fc = None, fill = False)
    ax.add_patch(circle1)
    plt.scatter(res_long, res_lat)
    
    total_tacos = np.size(lats[indx])
    num_res = find_restaurants(indx)
    print('There are %i tacos/burritos at %i different locations within %.2f miles of you'%(total_tacos,num_res,rad))
    
    return total_tacos

def find_restaurants(indx):
    all_res = restaurants[indx]
    all_res.flatten()
    un_res = []
    for res in all_res:
        if res not in un_res:
            un_res.append(res)
        else:
            pass
    return np.size(un_res)
    
num_tacos = find_tacos(my_lat, my_long, my_rad)