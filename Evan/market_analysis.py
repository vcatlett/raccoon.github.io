import csv
import re
from operator import itemgetter
import statistics as stat
import pprint

import numpy as np
import scipy.stats as sci

common_words = np.loadtxt('100_common_words.txt', dtype='str')

'''
load_US()

loads trimmed US data
'''
def load_US():
    with open('North_America_Only.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(data)
        #np.save('data.npy', data)
        csvfile.close()
    return data

def main():
    data = load_US()

    basic_stats = get_basic_stats(data)
    keywords = get_keywords(data)


def get_basic_stats(data):
    n_items = len(data)

    restaurants = []
    prices = []
    for i in range(0, len(data)):
        if data[i][0] is not in restaurants:
            restaurants.append(data[i][0])
            prices.append(data[i][24])
    n = len(restaurants)
    price_median = median(prices)
    price_mean = mean(prices)
    price_iqr = sci.iqr(prices)

    return f"{n},{n_items}\n{price_median},{price_mean},{price_iqr}\n"


def get_keywords(data):
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

    '''
    creates array of price statistics for each word in menus.description
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

    common_words = sorted(av_prices, key=itemgetter(1), reverse=True)
    common_words_str = ""
    for i in range(0, 5):
        common_words_str = f"{common_words_str},{common_words[i]}"
    common_words_str = f"{common_words_str}\n"

    expensive_words = sorted(av_prices, key=itemgetter(1), reverse=True)
    expensive_words_str = ""
    for i in range(0, 5):
        expensive_words_str = f"{expensive_words_str},{expensive_words[i]}"
    expensive_words_str = f"{expensive_words_str}\n"

    return f"{common_words_str}\n"

if __name__ == '__main__':
    main()
