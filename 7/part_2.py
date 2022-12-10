import re

cmd = [x.replace('\n', '').replace('/','root').split(' ') for x in open('day7.data')]
dircontains = {}
dirsize = {}
currdir = ''

while cmd:
        x = cmd[0]
        if len(x) == 3 and x[2] != '..':
            currdir = currdir + x[2] + '/'
            dircontains[currdir] = []
            dirsize[currdir] = 0
            cmd.remove(x)
        elif len(x) == 3 and x[2] == '..':
            currdir = currdir[:-1]
            currdir = currdir[:currdir.rfind('/')+1]
            cmd.remove(x)
        elif x[0] == 'dir':
            dircontains[currdir].append(currdir + x[1] + '/')
            for key, value in dircontains.items():
                if currdir in value:
                    dircontains[key].append(currdir + x[1] + '/')
            cmd.remove(x)
        elif re.match('^[0-9]',x[0]):
            dirsize[currdir] += int(x[0])
            for key, value in dircontains.items():
                if currdir in value:
                    dirsize[key] += int(x[0])
            cmd.remove(x)
        else:
            cmd.remove(x)

disk_space = 70000000
available_space = disk_space - dirsize[next(iter(dirsize))]
req_space = 30000000 - available_space

dir_candidates = []
for key, value in dirsize.items():
    if value >= req_space:
        dir_candidates.append(value)

#Part II answer:
print(min(dir_candidates))
