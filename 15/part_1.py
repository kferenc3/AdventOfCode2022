####################################################################################################################################### 
#   Most likely day 15 marks the end of my journey in AoC 2022. I thought I had a solution for part 1 as this works on the tiny       #
#   test array, but I didn't consider the real data's size. Looking at day 16 and day 17, the tasks are now a bit out of my league.   #
#   I will however try to complete each one sometimes in the future, but I would need to learn some more advanced stuff first.        #
#######################################################################################################################################

import os
import numpy as np
os.chdir(os.getcwd()+'/15')

def masking(s, b, maxx, maxy):
    x,y = s[0], s[1]
    r = abs(s[0]-b[0]) + abs(s[1]-b[1])
    c,d = np.ogrid[-x:maxx-x, -y:maxy-y]
    m = abs(c+c) + abs(d+d) <= 2*r
    return m

coords = [x.replace('\n','').replace('Sensor at ', '').replace(' closest beacon is at ','').replace('x=','').replace(' y=','').split(':') for x in open('day_15_test.data')]

# Manhattan distance = |x1-y1| + |x2-y2|

sensors = {}
beacons = {}
shift = 1000000000

max_x = 0
max_y = 0
for x in coords:
    i = min([int(y) for y in x[0].split(',')])
    j = min([int(y) for y in x[1].split(',')])
    k = max([int(y) for y in x[0].split(',')][0],[int(y) for y in x[1].split(',')][0])
    l = max([int(y) for y in x[0].split(',')][1],[int(y) for y in x[1].split(',')][1])
    if shift > min(i,j):
        shift = min(i,j)
    if max_x < k:
        max_x = k
    if max_y < l:
        max_y = l

max_x = max_x + abs(shift)+2
max_y = max_y + abs(shift)+2 

for i, x in enumerate(coords):
    sensors[i] = tuple(int(y)+abs(shift) for y in x[0].split(','))
    beacons[i] = tuple(int(y)+abs(shift) for y in x[1].split(','))

arr = np.full((max_x,max_y),None)

for key, value in sensors.items():
    s = sensors[key]
    b = beacons[key]
    print(abs(s[0]-b[0]) + abs(s[1]-b[1]))
    mask = masking(s,b,max_x,max_y)
    arr[mask] = 1

print(np.count_nonzero(arr[:,12]))