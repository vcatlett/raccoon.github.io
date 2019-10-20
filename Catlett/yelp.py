#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 02:57:19 2019

@author: victoriacatlett
"""
import json
import numpy as np
import pandas as pd

y_ids = []
addresses = []
names = []
citys = []
states = []
y_zips = []
y_lats = []
y_longs = []
ratings = []
review_counts = []

datapath = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/yelp_dataset/business.json'
for line in open(datapath, "r"):
    jline = json.loads(line)
    print(jline)
    name = jline['name']
    address = jline['address']
    y_id = jline['business_id']
    city = jline['city']
    state = jline['state']
    y_zip = jline['postal_code']
    y_lat = jline['latitude']
    y_long = jline['longitude']
    rating = jline['stars']
    review_count = jline['review_count']
    names.append(name)
    addresses.append(address)
    y_ids.append(y_id)
    citys.append(city)
    states.append(state)
    y_zips.append(y_zip)
    y_lats.append(y_lat)
    y_longs.append(y_long)
    ratings.append(rating)
    review_counts.append(review_count)
    print(jline['business_id'])
    print('\n')

df = pd.DataFrame({'name':names,'address':address,'y_id':y_ids, 'city':citys, 'state':states, 'y_zip':y_zips,'y_lat':y_lats, 'y_long':y_longs, 'rating':ratings, 'review_count':review_counts})
df.to_csv('/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/yelp_data.csv')