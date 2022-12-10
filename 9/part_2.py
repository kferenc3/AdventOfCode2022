#I intend to clean up the t_mover function to a bit nicer version, therefore the "neighbors" function. However for now this works as well for both parts.

#def neighbors(c1, c2):
    #lst = [[c3, c4] for c3, c4 in [(c1+1, c2), (c1-1, c2), (c1, c2+1), (c1, c2-1)]]
    #return lst

def t_mover(t,h):
    #n = neighbors(t[0],t[1])
    delta = [0,0]
    hd = h[1]-t[1]
    vd = h[0]-t[0]    
    
    if abs(hd) == 2 and abs(vd) == 0:
        delta[1] = 1 * hd//abs(hd)
    elif abs(vd) == 2 and abs(hd) == 0:
        delta[0] = 1 * vd//abs(vd)
    elif abs(hd) == 2 and abs(vd) == 1:
        delta = [1 * vd//abs(vd),1 * hd//abs(hd)]
    elif abs(hd) == 1 and abs(vd) == 2:
        delta = [1 * vd//abs(vd),1 * hd//abs(hd)]
    elif abs(hd) >= 2 and abs(vd) >= 2:
        delta = [1 * vd//abs(vd),1 * hd//abs(hd)]     
    elif delta == [0,0]:
        return t   
    new_t = [x+y for x,y in zip(t,delta)]
    return new_t
   

def h_mover(direction, steps, m):
    res = []
    if direction == 'L' or direction == 'D':
        x = -1
    else:
        x = 1

    if direction == 'R' or direction == 'L':
        coord = 1
    else:
        coord = 0

    for _ in range(steps):
        m[coord] += 1 * x
        res.append(m.copy())
    return res


if __name__ == '__main__':

    instructions = [(x, int(y)) for x,y in [z.split() for z in open('day_9_test.data')]]

    
    H = [0,0]
    moves = []
    visited = []
    temp_list = []
    ropes = {1: [0,0], 2: [0,0], 3: [0,0], 4: [0,0], 5: [0,0], 6: [0,0], 7: [0,0], 8: [0,0], 9: [0,0]}

    for x in instructions:
        for y in h_mover(x[0],x[1],H):
            moves.append(y)
    
    for key, value in ropes.items():
        for m in moves:
            ropes[key] = t_mover(ropes[key],m)
            if key == 9:
                if ropes[key] not in temp_list:
                    temp_list.append(ropes[key].copy())
            else:
                temp_list.append(ropes[key].copy())
        moves = temp_list.copy()
        temp_list = []
    
    "Part II answer"
    print(len(moves))
