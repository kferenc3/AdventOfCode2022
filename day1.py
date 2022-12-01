with open('day1.data') as f:
    lst = [int(i.replace('\n','')) if i != '\n' else '' for i in f]

cals =[]
c = 0
for x in lst:
    if x != '':
        c += int(x)
    else:
        cals.append(c)
        c=0

#Part 1 Answer:
print(max(cals))

#Part 2 Answer:
print(sum(sorted(cals,reverse=True)[:3]))

