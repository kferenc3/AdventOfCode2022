backpacks = [i.replace('\n','') for i in open('day_3_test.data')]
priority1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
priority2 = [i.upper() for i in priority1]

#PART II:
total = 0
while len(backpacks) != 0:
    elf1 = set(backpacks.pop(0))
    elf2 = set(backpacks.pop(0))
    elf3 = set(backpacks.pop(0))
    try:
        total += priority1.index(list((elf1 & elf2 & elf3))[0])+1
    except ValueError:
        total += priority2.index(list((elf1 & elf2 & elf3))[0])+27

#Part II answer:
print(total)