import os
import numpy as np
from skimage.draw import line_aa
import pandas as pd
os.chdir(os.getcwd() + '/14')

def cave_drawer(f):
    s = [x.strip().replace(' ', '').split('->') for x in open(f)]

    width = []
    height = []
    lines = []

    for x in s:
        l = []
        for y in x:
            l.append([int(z) for z in y.split(',')])
            width.append(int(y.split(',')[1]))
            height.append(int(y.split(',')[0]))
        lines.append(l)
    print(max(width)+2)
    print(max(height)+200)
    cave = np.full(shape=(max(width)+3,max(height)+200),fill_value='.')
    for line in lines:
        start = line.pop(0)
        while line:
            end = line.pop(0)
            rr,cc,val = line_aa(start[1],start[0],end[1],end[0])
            cave[rr,cc] = '#'
            start = end
    cave[0,500] = '+'
    
    rr,cc,val = line_aa(max(width)+2,0,max(width)+2,max(height)+195)
    cave[rr,cc] = '#'

    return cave

def neighbors(c1, c2, h, w, m):
    #Slightly modified "neighbors" function to the 3 bottom coordinates (straight down and diagonally)"
    n ={'d': [],'d_l': [], 'd_r': []}

    if 0 <= c1+1 <= h and 0 <= c2 < w and m[(c1+1, c2)] != '#' and m[(c1+1, c2)] != 'O':
        n['d'] = [c1+1, c2]
    if 0 <= c1+1 <= h and 0 <= c2-1 < w and m[(c1+1, c2-1)] != '#' and m[(c1+1, c2-1)] != 'O':
        n['d_l'] = [c1+1, c2-1]
    if 0 <= c1+1 <= h and 0 <= c2+1 < w and m[(c1+1, c2+1)] != '#' and m[(c1+1, c2+1)] != 'O':
        n['d_r'] = [c1+1, c2+1]
    
    return n

if __name__ == '__main__':
    cave = cave_drawer('day_14_test.data')
    

    sand_start = np.where(cave == '+')
    x,y = sand_start[0][0], sand_start[1][0]
    height, width = np.shape(cave)
    height = height - 1
    width = width -1
    new_sand = True

    while new_sand:
        x,y = sand_start[0][0], sand_start[1][0]
        n = []
        n = neighbors(x,y, height, width, cave)
        while neighbors:
            if len(n['d']) != 0:
                x,y = n['d']
                n = neighbors(x, y, height, width, cave)
            elif len(n['d_l']) != 0:
                x,y = n['d_l']
                n = neighbors(x, y, height, width, cave)
            elif len(n['d_r']) != 0:
                x,y = n['d_r']
                n = neighbors(x, y, height, width, cave)
            else:
                if cave[x,y] != 'O':
                    cave[x,y] = 'O'
                    break
                else:
                    new_sand = False
                    break
    
    #Part II answer
    print(np.sum(cave == 'O'))