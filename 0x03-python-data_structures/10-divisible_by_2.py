#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_ = []
    for n in range(len(my_list) + 1):
        if n % 2 == 0:
            list_.append(True)
        else:
            list_.append(False)
    return list_
