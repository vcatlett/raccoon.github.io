#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 05:26:37 2019

@author: victoriacatlett
"""

import json
import numpy as np
import pandas as pd

path = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/'

yelp_data = pd.read_csv(path + 'yelp_data.csv')
bigf = pd.read_csv(path + 'template_data_fully_filled.csv')
bigf = bigf.loc[:, ~bigf.columns.str.contains('^Unnamed')]

GS = []
Yelp = []
y_ids = []
addresses = []
cats = []
names = []
citys = []
countrys = []
states = []
y_zips = []
y_lats = []
y_longs = []
ratings = []
review_counts = []

for i in range(55596):
    GS.append(1)
    Yelp.append(0)
    ratings.append(np.nan)

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
    GS.append(0)
    Yelp.append(1)
    names.append(name)
    addresses.append(address)
    countrys.append(np.nan)
    cats.append(np.nan)
    y_ids.append(y_id)
    citys.append(city)
    states.append(state)
    y_zips.append(y_zip)
    y_lats.append(y_lat)
    y_longs.append(y_long)
    ratings.append(rating)
    review_counts.append(review_count)


bigf.append({'id':y_ids, 'address':addresses, 'categories':cats, 'city':citys,
       'country':countrys, 'cuisines':countrys, 'dateAdded':countrys, 'dateUpdated':countrys, 'keys':countrys, 'latitude':y_lats,
       'longitude':y_longs, 'menuPageURL':countrys, 'menus.amountMax':countrys, 'menus.amountMin':countrys,
       'menus.category':countrys, 'menus.currency':countrys, 'menus.dateSeen':countrys,
       'menus.description':countrys, 'menus.name':countrys, 'name':names, 'postalCode':y_zips,
       'priceRangeCurrency':countrys, 'priceRangeMin':countrys, 'priceRangeMax':countrys, 'province':states,
       'websites':countrys, 'R1':countrys, 'R5':countrys, 'R25':countrys, 'R50':countrys, 'R100':countrys, 'Item_Type':countrys,
       'Price_Score':countrys, 'Location':countrys}, ignore_index=True)
#bigf['GS?'] = GS
#bigf['Yelp?'] = Yelp
#bigf['Rating'] = ratings