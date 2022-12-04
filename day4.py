sections = [z.replace('\n','').split(',') for z in open('day4test.data')]

elf_1_ranges = []
elf_2_ranges = []

for x in sections:
    for y in range(len(x)):
        if y == 0:
            elf_1_ranges.append(set(range(int(x[y].split('-')[0]),int(x[y].split('-')[1])+1)))
        else:
            elf_2_ranges.append(set(range(int(x[y].split('-')[0]),int(x[y].split('-')[1])+1)))
  
i = 0
for x in range(len(elf_1_ranges)):
    if elf_1_ranges[x].issubset(elf_2_ranges[x]) or elf_1_ranges[x].issuperset(elf_2_ranges[x]):
        i += 1

#Part I answer
print(i)

i = 0

for x in range(len(elf_1_ranges)):
    if not elf_1_ranges[x].isdisjoint(elf_2_ranges[x]):
        i += 1

#Part II answer
print(i)
