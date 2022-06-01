#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (0rd('a') - ord('A')))
        print("{:s}".format(c), end='')
    print("")
