#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:07:15 2019

@author: victoriacatlett
"""

import numpy as np
import pandas as pd

pathname = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/'
filename = 'North_America_Only.csv'

data = pd.read_csv(pathname + filename)
data['R1'] = np.nan
data['R5'] = np.nan
data['R25'] = np.nan
data['R50'] = np.nan
data['R100'] = np.nan
data['Item_Type'] = np.nan
data['Price_Score'] = np.nan

data['Location'] = np.nan
data['Location'][0] = 30.6066
data['Location'][1] = -96.3568
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

data.to_csv(pathname + 'template_data.csv')