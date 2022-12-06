def char_parser(flnm, charlen):
    raw = open(flnm).readline()
    for x in range(len(raw)):
        if len(raw[x:x+charlen]) == len(set(raw[x:x+charlen])):
            return x+charlen


if __name__ == '__main__':

    #Part I answer:
    print(char_parser('day6.data',4))
    #Part II answer:
    print(char_parser('day6.data',14))
