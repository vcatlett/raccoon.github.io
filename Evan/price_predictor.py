import csv
import re
import pprint

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


'''
load_US()

loads trimmed US data on keywords
'''
def load_US():
    with open('US_keyword_rankings.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(data)
        #np.save('data.npy', data)
        csvfile.close()
    return data


'''
load_data()

loads all US data
'''
def load_data():
    '''
    loads trimmed data
    '''
    with open('North_America_Only.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(data)
        data = data[1:]
        #np.save('data.npy', data)
        csvfile.close()
    return data

US_KEYWORDS = load_US()
US_KEYWORDS_LIST = []
for i in range(0, len(US_KEYWORDS)):
    US_KEYWORDS_LIST.append(US_KEYWORDS[i][0])

ALL_DATA = load_data()

# def main():
#     keyword_data = load_US()
#     keywords = []
#     for x in keyword_data:
#         keywords.append(x[0])
#
#     all_data = load_data()
#     data_keywords = []
#     data_prices = []
#     for i in range(1, 100):
#         if all_data[i][18] != '' and all_data[i][24] != '':
#             desc = all_data[i][18].lower()
#             #print(desc)
#             spliced_desc = re.findall(r'\w+', desc)
#             #print(data[i][24])
#             price = float(all_data[i][24])
#
#             entry = []
#             for j in range(0, len(keywords)):
#                 if keywords[j] in spliced_desc:
#                     entry.append(1)
#                 else:
#                     entry.append(0)
#             data_keywords.append(entry)
#             data_prices.append(price)
#
#     x = np.array(data_keywords)
#     y = np.array(data_prices)
#
#     beta = LinearRegression().fit(x,y)
#     # # Finds inverse of X`X since it is square
#     # x_inv = np.linalg.inv(np.matmul(x.T, x))
#     #
#     # # Multiplies remaining matrices and vectors
#     # xt_y = np.matmul(x.T, y)
#     # beta = np.matmul(x_inv, xt_y)
#
#     with open('beta.csv', 'w') as outfile:
#         for i in range(0, len(beta.coef_)):
#             outfile.write(f'{beta.coef_[i]}\n')
#         outfile.write(f'{beta.intercept_}\n')
#         outfile.close()
#     print(beta)


def main():

    descriptions = []
    prices = []
    for i in range(0, len(ALL_DATA)):
        # Trim to only include entries with both value sets!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if ALL_DATA[i][18] != '' and ALL_DATA[i][24] != '':
            descriptions.append(ALL_DATA[i][18])
            prices.append(float(ALL_DATA[i][24]))
    x_train, x_test, y_train, y_test = train_test_split(descriptions, prices, test_size=.01)
    output = []
    for i in range(0, len(x_test)):
        output.append([y_test[i], predict(x_test[i])])
    pp = pprint.PrettyPrinter()
    pp.pprint(output)


def predict(line):
    line = line.lower()
    keywords = re.findall(r'\w+', line)
    n = len(keywords)
    if n > 0:
        sum = 0
        for x in keywords:
            if x in US_KEYWORDS_LIST:
                index = US_KEYWORDS_LIST.index(x)
                sum += float(US_KEYWORDS[index][3])
        sum /= n
    else:
        sum = ABS_AV   # Average price for all items
    return sum


def deal(line, price):
    return predict(line) / price


def score(line, price, sentiment):
    return sentiment * deal(line, price)


if __name__ == '__main__':
    main()
