import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
radii = [1.0, 5.0, 25.0, 50.0, 100.0]
col_names = ['R1', 'R5', 'R25', 'R50', 'R100']

lats = data['latitude'].values
longs = data['longitude'].values

c_earth = 24901.

def find_tacos(user_lat, user_long):
    for i in range(len(radii)):
        rad = radii[i]
        res_theta = (rad/c_earth)*360.
        dist = np.square(lats-user_lat)+np.square(longs-user_long)
        indx = np.where(dist <= (res_theta**2))
        
        res_lat = lats[indx]
        res_long = longs[indx]
        
        fig, ax = plt.subplots(1)
        plt.plot(user_long, user_lat, 'or')
        circle1 = plt.Circle((user_long, user_lat), radius = res_theta, ec = 'r', fc = None, fill = False)
        ax.add_patch(circle1)
        plt.scatter(res_long, res_lat)
        #print(np.where(dist <= (res_theta**2), True, False))
        data[col_names[i]] = np.where(dist <= (res_theta**2), True, False)
        print(np.where(data[col_names[i]]==True)[0])
    data.to_csv('data.csv')