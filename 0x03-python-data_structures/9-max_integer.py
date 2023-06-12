#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max_ = my_list[0]
    for num in my_list[1:]:
        if num > max_:
            max_t = num
    return max_
