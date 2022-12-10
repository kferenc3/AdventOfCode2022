
def inputprocessor(f):
    ins = []
    for i in [ln.split() for ln in open(f)]:
        if len(i) == 2:
            ins.append(i[0])
            ins.append(int(i[1]))
        else:
            ins.append(i[0])
    return ins

instructions = inputprocessor('day10.data')
x = 1
y = 0
cycle = 1
strength = 0
while cycle != 221:
    x += y
    y = 0
    if cycle  in [20, 60, 100, 140, 180, 220]:
        strength += x * cycle
    i = instructions.pop(0)
    if i == 'addx' or i == 'noop':
        pass
        cycle += 1
    else:
        y += i
        cycle +=1
    
# Part I answer:
print(strength)
