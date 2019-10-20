import csv
import re
from operator import itemgetter
import statistics as stat
import pprint

import numpy as np
#import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
import scipy.stats as sci

# headers = np.load('headers.npy')
# data = np.load('data.npy')
#
# new_data = []
# for i in range(0, len(data)):
#     if float(data[i][9]) > 0 and float(data[i][10]) < -50:
#         new_data.append(data[i])
# print(len(new_data))

'''
loads trimmed data
'''
with open('North_America_Only.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    data = list(data)
    #np.save('data.npy', data)
    csvfile.close()

'''
loads words
'''
with open('taco-burrito-desc-words.csv', 'r') as csvfile:
    words = csv.reader(csvfile, delimiter=',', quotechar='"')
    words = list(words)
    #np.save('data.npy', data)
    csvfile.close()

'''
loads 100 most common words from gutenberg project
'''
common_words = np.loadtxt('100_common_words.txt', dtype='str')

# km = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1, init_size=1000, batch_size=1000, verbose=opts.verbose)
# km.fit(words)

# print(data[5])
# print(data[5][17])
# print(data[5][23])
prices = {}
for i in range(1, len(data)):
    if data[i][18] != '' and data[i][24] != '':
        desc = data[i][18].lower()
        #print(desc)
        spliced_desc = re.findall(r'\w+', desc)
        #print(data[i][24])
        price = float(data[i][24])
        for x in spliced_desc:
            if x in prices.keys():
                prices[x].append(price)
            else:
                prices[x] = [price]
#print(len(prices['cheese']))
#print(prices.keys())
#print(prices['octopus'])

'''
creates dictionary of average prices for each word in menus.description
'''
# av_prices = {}
# for key in prices.keys():
#     av_prices[key] = sum(prices[key]) / len(prices[key])
# print(av_prices)

'''
creates array of average prices for each word in menus.description
'''
av_prices = []
for key in prices.keys():
    if key not in common_words:
        n = len(prices[key])
        if n >= 10:
            med = stat.median(prices[key])
            av = stat.mean(prices[key])
            sd = stat.stdev(prices[key])
            rng = max(prices[key]) - min(prices[key])
            iqr = sci.iqr(prices[key])
            av_prices.append([key, n, med, av, sd, rng, iqr])
    av_prices = sorted(av_prices, key=itemgetter(1), reverse=True)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(av_prices)
print(len(av_prices))



with open('US_keyword_rankings.csv', 'w') as fid:
    for i in range(0, len(av_prices)):
        for j in range(0, len(av_prices[i])):
            fid.write(f'{av_prices[i][j]}')
            if j != len(av_prices[i]) - 1:
                fid.write(',')
        fid.write(f'\n')
    fid.close()
# av_prices = np.array(av_prices)
# np.savetxt("US_keyword_rankings.csv", av_prices, delimiter=',', encoding='str')
