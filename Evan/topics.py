import csv
import re

import numpy as np


T_COL = 33

with open('template_data.csv', 'r') as csvfile:
    ALL_DATA = csv.reader(csvfile, delimiter=',', quotechar='"')
    ALL_DATA = list(ALL_DATA)
    #np.save('data.npy', data)
    csvfile.close()

with open('word_betas.csv', 'r') as csvfile:
    WORD_BETAS = csv.reader(csvfile, delimiter=',', quotechar='"')
    WORD_BETAS = list(WORD_BETAS)
    #np.save('data.npy', data)
    csvfile.close()

classes = []
for i in range(1, len(ALL_DATA)):
    line = ALL_DATA[i][20].lower()
    spliced_line = re.findall(r'\w+', line)
    print(spliced_line)
    if len(spliced_line) > 0:
        weights = [0] * 10
        for j in range(1, len(WORD_BETAS)):
            if WORD_BETAS[j][1] in spliced_line:
                index = int(WORD_BETAS[j][0]) - 1
                weights[index] += float(WORD_BETAS[j][2])
        print(weights)
        maximum = max(weights)
        classification = weights.index(maximum)
        print(classification)
        ALL_DATA[i][T_COL] = classification

with open('template_data_filled.csv', 'w') as outfile:
    item_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(ALL_DATA)):
        item_writer.writerow(ALL_DATA[i])
    outfile.close()

# with open('classes.txt', 'w') as outfile:
#     outfile.write(f'item_type\n')
#     for i in range(0, len(classes)):
#         outfile.write(f'{classes[i]}\n')
#     outfile.close()
