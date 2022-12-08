import re
#This doesn't work (obviously works on the test, because why not), but I spent so much time on this task that 
#I think this needs to be in the repository just as a memento of pain and suffering
cmd = [x.replace('\n', '').replace('/', 'root').split(' ') for x in open('day7.data')]
dircontains = {}
dirsize = {}
while cmd:
        x = cmd[0]
        if len(x) == 3 and x[2] != '..':
            currdir = x[2]
            dircontains[currdir] = []
            dirsize[currdir] = 0
            cmd.remove(x)
        elif len(x) == 3 and x[2] == '..':
            cmd.remove(x)
        elif x[0] == 'dir':
            dircontains[currdir].append(x[1])
            cmd.remove(x)
        elif re.match('^[0-9]',x[0]):
            dirsize[currdir] += int(x[0])
            for key, value in dircontains.items():
                if currdir in value:
                    dirsize[key] += int(x[0])
            cmd.remove(x)
        else:
            cmd.remove(x)

total = 0
for key, value in dirsize.items():
    if value <= 100000:
        total += value
