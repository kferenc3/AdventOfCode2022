lst = [int(i.replace('\n','')) if i != '\n' else '' for i in open('day_1_test.data')]

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