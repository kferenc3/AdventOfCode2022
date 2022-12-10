
def data_processor(f: str):
    sections = [z.replace('\n','').split(',') for z in open(f)]
    e1 = []
    e2 = []
    for x in sections:
        for y in range(len(x)):
            if y == 0:
                e1.append(set(range(int(x[y].split('-')[0]),int(x[y].split('-')[1])+1)))
            else:
                e2.append(set(range(int(x[y].split('-')[0]),int(x[y].split('-')[1])+1)))
    return e1, e2

def partial_overlap(e1,e2):
    i = 0
    for x in range(len(e1)):
        if not e1[x].isdisjoint(e2[x]):
            i += 1
    return i


if __name__ == '__main__':
    
    elf_1_ranges, elf_2_ranges = data_processor('day_4_test.data')
    
    #Part II answer
    print(partial_overlap(elf_1_ranges,elf_2_ranges))
