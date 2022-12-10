import numpy as np

def coords(m):
    lst = []
    for x, y in np.ndenumerate(m):
        lst.append(x)
    return lst

def neighbors(c1, c2, h, w):
    lst = [(c3, c4) for c3, c4 in [(c1+1, c2), (c1-1, c2), (c1, c2+1), (c1, c2-1)]
           if 0 <= c3 < h and 0 <= c4 < w]
    return lst

def directions(x, height, width):
    col = []
    row = []
    s = []
    for y in range(height):
        col.append((y,x[1]))
    for y in range(width):
        row.append((x[0],y))
    s.append(col[:x[0]]) # -->
    s.append(col[x[0]+1:]) # <--
    s.append(row[:x[1]]) # -->
    s.append(row[x[1]+1:]) # <--
    return s

def scorer(x, height, width):
    m1,m2,m3,m4 = 0,0,0,0
    dir = directions(x, height, width)
    dir[1].reverse()
    dir[3].reverse()
    while dir[0]:
        if trees[dir[0][-1]] < trees[x]:
            m1 += 1
            dir[0].pop()
        elif trees[dir[0][-1]] >= trees[x]:
            m1 += 1
            break
    while dir[2]:
        if trees[dir[2][-1]] < trees[x]:
            m2 += 1
            dir[2].pop()
        elif trees[dir[2][-1]] >= trees[x]:
            m2 += 1
            break
    while dir[1]:
        if trees[dir[1][-1]] < trees[x]:
            m3 += 1
            dir[1].pop()
        elif trees[dir[1][-1]] >= trees[x]:
            m3 += 1
            break 
    while dir[3]:
        if trees[dir[3][-1]] < trees[x]:
            m4 += 1
            dir[3].pop()
        elif trees[dir[3][-1]] >= trees[x]:
            m4 += 1
            break
    
    return m1*m2*m3*m4


if __name__ == '__main__':

    trees = np.asarray([[int(col) for col in row.replace('\n', '')] for row in open('day_8_test.data')])
    coords = coords(trees)
    height, width = np.shape(trees)
    visible = []
    scenic_scores = []

    for x in coords:
        if len(neighbors(x[0], x[1], height, width)) < 4:
            pass
        else:
            scenic_scores.append(scorer(x, height, width))
            
    #Part II answer:
    print(max(scenic_scores))
