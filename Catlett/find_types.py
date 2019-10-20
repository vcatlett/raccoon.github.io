#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:39:36 2019

@author: victoriacatlett
"""
import numpy as np
import pandas as pd

pathname = '/Users/victoriacatlett/Desktop/TAMU_Datathon/Data/'
indv_words = pd.read_csv(pathname + 'taco-burrito-desc-words.csv')
groups = pd.read_csv(pathname + 'top_terms.csv')
data = pd.read_csv(pathname + 'template_data.csv')

top_words = groups['term']
topics = pd.to_numeric(groups['topic'])
current_indx = 0
types = [[],[]]
for i in range(20):
#for i in range(55597):
    words = str(data['menus.description'][i]).split()
    for ind_word in words:
        indx = np.where(ind_word == top_words)[0]
        ind_topics = topics[indx]
        print(ind_topics)