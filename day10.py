def lineselector(cycle, screen):
    if 1 <= cycle <= 40:
        return screen[0]
    if 41 <= cycle <= 80:
        return screen[1]
    if 81 <= cycle <= 120:
        return screen[2]
    if 121 <= cycle <= 160:
        return screen[3]
    if 161 <= cycle <= 200:
        return screen[4]
    if 201 <= cycle <= 240:
        return screen[5]

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

instructions = inputprocessor('day10.data')
x = 1
y = 0
cycle = 1
pos = 0
ln1 = []
ln2 = [] 
ln3 = [] 
ln4 = []
ln5 = []
ln6 = []

screen = [ln1,ln2,ln3,ln4,ln5,ln6]
while cycle != 241:
    currline = lineselector(cycle, screen)
    x += y
    y = 0
    if x -1 == pos or x == pos or x+1 == pos:
        currline.append('#')
    else:
        currline.append('.')
    i = instructions.pop(0)
    if i == 'addx' or i == 'noop':
        pass
        cycle += 1
        if pos+1 == 40:
            pos = 0
        else:
            pos += 1 
    else:
        y += i
        cycle +=1
        if pos+1 == 40:
            pos = 0
        else:
            pos += 1

print(''.join(ln1)+'\n'+''.join(ln2)+'\n'+''.join(ln3)+'\n'+''.join(ln4)+'\n'+''.join(ln5)+'\n'+''.join(ln6)+'\n')
