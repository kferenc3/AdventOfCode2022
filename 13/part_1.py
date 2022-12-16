import os
from ast import literal_eval
os.chdir(os.getcwd() + '/13')

class Pairs(object):
    
    def __init__(self, pairs):
        self.left = pairs[0]
        self.right = pairs[1]
    
    def comparer(self, l, r):
        if isinstance(l, int) and isinstance(r, int):
            int_l = l
            int_r = r
            if int_l == int_r:
                return None
            elif int_l > int_r:
                return False
            elif int_l < int_r:
                return True
        if isinstance(l, list) and isinstance(r, int):
            r = [r]
        if isinstance(l, int) and isinstance(r, list):
            l = [l]
        if isinstance(l, list) and isinstance(r, list):
            for x in range(max(len(l),len(r))):
                try:
                    l_i = l.pop(0)
                except IndexError:
                    #left ran out of items
                    return True
                try:
                    r_i = r.pop(0)
                except IndexError:
                    #right ran out of items
                    return False
                res = self.comparer(l_i,r_i)
                if res is not None:
                    return res

    def solve(self):
        return self.comparer(self.left,self.right)



if __name__ == '__main__':
    raw = [literal_eval(x.replace('\n','')) for x in open('day_13_test.data') if x != '\n']

    right_order = []
    pairs_dict = {}
    
    for x in range(1,len(raw)//2+1):
        pairs_dict[x] = [raw.pop(0),raw.pop(0)]

    for key, value in pairs_dict.items(): 
        p = Pairs(pairs_dict[key])
        if p.solve():
            right_order.append(key)

    #Part I answer:
    print(sum(right_order))

