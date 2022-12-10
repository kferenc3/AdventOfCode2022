backpacks = [i.replace('\n','') for i in open('day_3_test.data')]
priority1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
priority2 = [i.upper() for i in priority1]

#PART I
total = 0
for content in backpacks:
    comp1 = set(content[:len(content)//2])
    comp2 = set(content[len(content)//2:])
    try:
        total += priority1.index(str(list((comp1 & comp2))[0]))+1
    except ValueError:
        total += priority2.index(str(list((comp1 & comp2))[0]))+27

#Part I answer:
print(total)