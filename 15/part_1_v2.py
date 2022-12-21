####################################################################################################################################### 
# Alternative solution attempt                                                                                                        #
#######################################################################################################################################

import os
import numpy as np
import pandas as pd
os.chdir(os.getcwd()+'/15')

coords = [x.replace('\n','').replace('Sensor at ', '').replace(' closest beacon is at ','').replace('x=','').replace(' y=','').split(':') for x in open('day_15_test.data')]

# Manhattan distance = |x1-y1| + |x2-y2|

sensors = {}
beacons = {}

max_x = 0
max_y = 0
min_x = 1000000000
min_y = 1000000000
for x in coords:
    i = min([int(y) for y in x[0].split(',')][0],[int(y) for y in x[1].split(',')][0])
    k = max([int(y) for y in x[0].split(',')][0],[int(y) for y in x[1].split(',')][0])
    l = max([int(y) for y in x[0].split(',')][1],[int(y) for y in x[1].split(',')][1])
    m = min([int(y) for y in x[0].split(',')][1],[int(y) for y in x[1].split(',')][1])
    if min_x > i:
        min_x = i
    if max_x < k:
        max_x = k
    if max_y < l:
        max_y = l
    if min_y > m:
        min_y = m

dist_list = {}

for i, x in enumerate(coords):
    sensors[i] = tuple(int(y) for y in x[0].split(','))
    beacons[i] = tuple(int(y) for y in x[1].split(','))
    dist_list[i] = (abs(sensors[i][0]-beacons[i][0]) + abs(sensors[i][1]-beacons[i][1]))

#Y = 2000000 #full
Y = 10 #test
distress_isnt =[]
for i in range(min_x-max(dist_list.values()),max_x+max(dist_list.values())):
    for key, value in sensors.items():
        r = abs(value[0]-i) + abs(value[1]-Y)
        if r <= dist_list[key]:
            if (i,Y) not in list(beacons.values()):
                distress_isnt.append(i)
                break

print(len(distress_isnt))


# print(np.count_nonzero(arr[:,12]))