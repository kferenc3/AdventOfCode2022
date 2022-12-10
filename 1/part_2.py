lst = [int(i.replace('\n','')) if i != '\n' else '' for i in open('test.data')]

cals =[]
c = 0
for x in lst:
    if x != '':
        c += int(x)
    else:
        cals.append(c)
        c=0

#Part 2 Answer:
print(sum(sorted(cals,reverse=True)[:3]))

