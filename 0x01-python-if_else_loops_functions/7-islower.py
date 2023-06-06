#!/usr/bin/python3
low_list = []


def islower(c):
    for n in range(97, 123):
        low_list.append(chr(n))
    if c in low_list:
        return True
    return False
