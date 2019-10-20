import csv

with open('template_data.csv', 'r') as csvfile:
    ALL_DATA = csv.reader(csvfile, delimiter=',', quotechar='"')
    ALL_DATA = list(ALL_DATA)
    #np.save('data.npy', data)
    csvfile.close()

with open('classes.csv', 'r') as csvfile:
    CLASSES = csv.reader(csvfile, delimiter=',', quotechar='"')
    CLASSES = list(CLASSES)
    #np.save('data.npy', data)
    csvfile.close()

for i in range(1, len(ALL_DATA)):
    ALL_DATA[i][-3] = CLASSES[i]

with open('template_data_filled.csv', 'w') as outfile:
