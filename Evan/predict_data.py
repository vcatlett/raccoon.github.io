import csv
import re
import statistics as stat
from operator import itemgetter

import numpy as np
import scipy.stats as sci


C_COL = 33   # Column of classification from topic methods
ST_COL = 35   # Column of sentiment analysis score
SC_COL = 34   # Column of ranking score

ABS_AV = 0
common_words = np.loadtxt('100_common_words.txt', dtype='str')


def main():
    global ABS_AV
    with open('template_data_filled.csv', 'r') as csvfile:
        ALL_DATA = csv.reader(csvfile, delimiter=',', quotechar='"')
        ALL_DATA = list(ALL_DATA)
        #np.save('data.npy', data)
        csvfile.close()

    sum = 0
    count = 0
    for i in range(1, len(ALL_DATA)):
        if ALL_DATA[i][25] != '':
            sum += float(ALL_DATA[i][25])
            count += 1
    ABS_AV = sum / count

    data_classes = {}
    for i in range(0, len(ALL_DATA)):
        classification = ALL_DATA[i][C_COL]
        if classification in data_classes:
            data_classes[classification].append(ALL_DATA[i])
        else:
            data_classes[classification] = [ALL_DATA[i]]

    class_stats = {}
    for key in data_classes.keys():
        class_stats[key] = get_stats(data_classes[key])
    print(class_stats)
    sum = 0
    count= 0
    for i in range(1, len(ALL_DATA)):
        type = ALL_DATA[i][C_COL]
        sc = score(ALL_DATA[i], class_stats[type])
        ALL_DATA[i][SC_COL] = sc
        if sc > 0:
            sum += sc
            count += 1
    print(1 / (sum / count))

    with open('template_data_filled_2.csv', 'w') as outfile:
        item_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(ALL_DATA)):
            item_writer.writerow(ALL_DATA[i])
        outfile.close()


def get_stats(data):
    prices = {}
    for i in range(1, len(data)):
        if data[i][19] != '' and data[i][24] != '':
            desc = data[i][19].lower()
            #print(desc)
            spliced_desc = re.findall(r'\w+', desc)
            #print(data[i][24])
            price = float(data[i][25])
            for x in spliced_desc:
                if x in prices.keys():
                    prices[x].append(price)
                else:
                    prices[x] = [price]

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

    av_prices_list = []
    for i in range(0, len(av_prices)):
        av_prices_list.append(av_prices[i][0])
    return av_prices, av_prices_list

def score(entry, class_stats):
    return deal(entry, class_stats)


def deal(entry, class_stats):
    line = entry[19].lower()
    spliced_line = re.findall(r'\w+', line)
    if len(spliced_line) > 0 and entry[25] != '':
        return predict(spliced_line, class_stats[0], class_stats[1]) / float(entry[25])
    else:
        return 1

def predict(spliced_line, stats, stats_list):
    n = len(spliced_line)
    sum = 0
    for x in spliced_line:
        if x in stats_list:
            index = stats_list.index(x)
            sum += float(stats[index][3])
    sum = 1.277715602083037 * sum / n
    return sum


if __name__ == '__main__':
    main()
