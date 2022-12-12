import os
import re
import math
os.chdir(os.getcwd()+'/11')

def input_parser(f):
    lst = [x.replace('\n','') for x in open(f)]
    m_i = {key: value for key,value in zip([int(x[-2]) for x in lst if x.startswith('M')],
                                                    [x.replace('  Starting items:','').split(',') for x in lst if x.startswith('  S')])}
    for key, value in m_i.items():
        m_i[key] = [int(x) for x in value]

    m_o = {key: value for key,value in zip([int(x[-2]) for x in lst if x.startswith('M')],
                                                    [x.replace('  Operation: new = old ','').split(' ') for x in lst if x.startswith('  O')])}

    m_t = {key: [value] for key,value in zip([int(x[-2]) for x in lst if x.startswith('M')],
                                                    [int(re.search('[0-9]*$',x).group()) for x in lst if x.startswith('  T')])}
    true_false_list = [int(re.search('[0-9]*$',x).group()) for x in lst if x.startswith('    I')]

    for key, value in m_t.items():
        value.append(true_false_list.pop(0))
        value.append(true_false_list.pop(0))
        m_t[key] = value
    
    return m_i, m_o, m_t

def calc_worry_level(monkey, item, m_o, divider):
    if m_o[monkey][0] == '*':
        try:
            item = (item * int(m_o[monkey][1]))
        except ValueError:
            item = (item * item)
    elif m_o[monkey][0] == '+':
        item = (item + int(m_o[monkey][1]))
    
    return math.floor(item%divider)


if __name__ == '__main__':

    inspections = {}
    monkey_items, monkey_operation, monkey_test = input_parser('day_11_full.data')
    ins = 0
    divisibles = [m[0] for m in monkey_test.values()]
    divider = math.prod(m for m in divisibles)
    for x in range(10000):
        for monkey, items in monkey_items.items():
            if items:
                while items:
                    items[0] = calc_worry_level(monkey, items[0], monkey_operation, divider)
                    if items[0] % monkey_test[monkey][0] == 0:
                        monkey_items[monkey_test[monkey][1]].append(items[0])
                    else:
                        monkey_items[monkey_test[monkey][2]].append(items[0])
                    try:
                        inspections[monkey] += 1
                    except KeyError:
                        inspections[monkey] = 1
                    items.pop(0)
    
    
    #Part II answer:
    print(sorted(list(inspections.values()),reverse=True)[0]*sorted(list(inspections.values()),reverse=True)[1])
   