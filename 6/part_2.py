def char_parser(flnm, charlen):
    raw = open(flnm).readline()
    for x in range(len(raw)):
        if len(set(raw[x:x+charlen])) == charlen:
            return x+charlen


if __name__ == '__main__':

    #Part II answer:
    print(char_parser('day_6_test.data',14))
