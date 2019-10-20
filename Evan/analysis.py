'''
Evan/analysis.py

Basic analysis of taco and burrito dataset.

'''

import gc

import numpy as np

gc.collect()
# data = np.loadtxt("just tacos and burritos.csv", dtype='str')


def load_data():
    with open('just tacos and burritos.csv', 'r') as file:
        raw_headers = file.readline().split(",")
        headers = np.array(raw_headers)
        content = []
        line = file.readline()
        while line:
            split_line = line.split(',')
            # line_dict = {}
            # for i in range(0, len(split_line)):
            #     x = split_line[i]
            #     if x != '':
            #         line_dict[headers[i]] = x
            # content.append(dict)
            content.append(split_line[0:26])
            line = file.readline()
        data = np.array(content)
        file.close()

    print(data.shape)
    np.save('headers', headers)
    np.save('data', data)

def main():
    #load_data()
    headers = np.load('headers.npy')
    data = np.load('data.npy')
    trimmed_headers = headers[0:26]
    np.save('headers', trimmed_headers)
    headers = np.load('headers.npy')
    print(headers.shape)
    print(data.shape)


if __name__ == '__main__':
    main()
