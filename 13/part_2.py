import os
from ast import literal_eval
import collections
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
                    l_i = l[x]
                except IndexError:
                    #left ran out of items
                    return True
                try:
                    r_i = r[x]
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
    raw.append([[2]])
    raw.append([[6]])
    sorted_codes = []
    code_dict = {}
   
    for code in raw:
        smaller = []
        to_check = code
        for x in range(len(raw)):
            if to_check == raw[x]:
                pass
            else:
                p = Pairs([to_check, raw[x]])
                if not p.solve():
                    smaller.append(raw[x])
        code_dict[len(smaller)+1] = code
    dividers = dict(filter(lambda e: e[1] == [[2]] or e[1] == [[6]],code_dict.items()))
    
    #Part II answer:
    print(list(dividers.keys())[0] * list(dividers.keys())[1])
    