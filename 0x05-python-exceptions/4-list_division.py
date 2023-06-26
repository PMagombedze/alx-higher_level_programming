#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division_list = []
    for n in range(list_length):
        res = 0
        try:
            res = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            division_list.append(res)

    return division_list
