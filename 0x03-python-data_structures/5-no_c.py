#!/usr/bin/python3
def no_c(my_string):
    my_list = []
    for letter in my_string:
        if letter != "C" and letter != "c":
            my_list.append(letter)
    return "".join(my_list)
