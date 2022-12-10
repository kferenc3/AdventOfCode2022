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


def visibility(x, height, width):
    if len(neighbors(x[0], x[1], height, width)) < 4:
        v = 4
    else:
        slices = directions(x, height, width)
        v = 0
        s = 0
        for y in slices:
            for g in y:
                if trees[g] >= trees[x]:
                    s += 1
            if s < 1:
                v += 1
                s = 0
            else:
                s = 0
    return v

if __name__ == '__main__':

    trees = np.asarray([[int(col) for col in row.replace('\n', '')] for row in open('day_8_test.data')])
    coords = coords(trees)
    height, width = np.shape(trees)
    visible = []
    scenic_scores = []

    for x in coords:
        if visibility(x,height,width) > 0:
            visible.append(x)

    #Part I answer:
    print(len(visible))
