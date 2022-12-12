import os
import numpy as np
import string
import heapq

os.chdir(os.getcwd() + '/12')

def neighbors(c1, c2, h, w, m):
    lst = [(c3, c4) for c3, c4 in [(c1, c2+1), (c1, c2-1), (c1+1, c2), (c1-1, c2)]
           if 0 <= c3 < h and 0 <= c4 < w and m[(c3, c4)] != -1]
    return lst

if __name__ == '__main__':

    heights = {key: value for key, value in zip(string.ascii_lowercase,[x for x in range(26)])}
    heights['S'] = 0
    heights['E'] = 25
    low_points = []
    alpha_map = np.asarray([[col for col in row.replace('\n', '') if col] for row in open('day_12_full.data')])
    num_map = np.full(alpha_map.shape,-1)
    
    
    for index in np.ndindex(num_map.shape):
        num_map[index] = heights[alpha_map[index]]
        if heights[alpha_map[index]] == 0:
            low_points.append(index)
    
    trails = []
    E = tuple(np.argwhere(alpha_map == 'E')[0])
    
    maxx, maxy = alpha_map.shape

    for l in low_points:
        for index in np.ndindex(num_map.shape):
            num_map[index] = heights[alpha_map[index]]
        S = l
        h = []
        heapq.heapify(h)
        x,y = S[0], S[1]
        dist_matrix = np.full(alpha_map.shape, 0)
        dist_matrix[S] = 0
        while x < maxx and y < maxy:
            if x == E[0] and y == E[1]:
                trails.append(dist_matrix[E])
                break
            else:
                if num_map[(x, y)] != -1:
                    for c in neighbors(x,y,maxx,maxy, num_map):
                        x2,y2 = c
                        if num_map[(x2, y2)] == num_map[(x, y)]+1:
                            dist_matrix[(x2, y2)] = dist_matrix[(x, y)] + 1
                            heapq.heappush(h,(dist_matrix[(x2,y2)], (x2,y2)))
                        elif num_map[(x2, y2)] == num_map[(x, y)]:
                            dist_matrix[(x2, y2)] = dist_matrix[(x, y)] + 1
                            heapq.heappush(h,(dist_matrix[(x2,y2)], (x2,y2)))
                        elif num_map[(x2, y2)] < num_map[(x, y)]:
                            dist_matrix[(x2, y2)] = dist_matrix[(x, y)] + 1
                            heapq.heappush(h,(dist_matrix[(x2,y2)], (x2,y2)))

            num_map[(x, y)] = -1 
            try:
                x,y = heapq.heappop(h)[1]
            except IndexError:
                # This means that from that point given the rules E is not reachable
                trails.append(10000)
                break
    #Part II answer:
    print(min(trails))
    

    
    
    #         print('part 2: '+str(dist_matrix[(maxx-1, maxy-1)]))
    #         break
    # 
    # dist_matrix[(0, 0)] = 0
    # unvisited[(0, 0)] = 0
    # maxx, maxy = unvisited.shape
    # h = []
    # heapq.heapify(h)

    # x,y = 0, 0
    # while x < maxx and y < maxy:
    #     if x == maxx-1 and y == maxy-1:
    #         print('part 2: '+str(dist_matrix[(maxx-1, maxy-1)]))
    #         break
    #     else:
    #         if unvisited[(x, y)] != -1:
    #             for c in neighbors(x,y,maxx,maxy, unvisited):
    #                 x2,y2 = c
    #                 if dist_matrix[(x2, y2)] > dist_matrix[(x, y)] + ((unvisited[(x2, y2)] % 9)+1):
    #                     dist_matrix[(x2, y2)] = dist_matrix[(x, y)] + ((unvisited[(x2, y2)] % 9)+1)
    #                     heapq.heappush(h,(dist_matrix[(x2,y2)], (x2,y2)))

    #     unvisited[(x, y)] = -1
    #     x,y = heapq.heappop(h)[1]
    #     if x == 99 and y == 99:
    #         print('part 1: ' + str(dist_matrix[(99, 99)]))