#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        print()
        return
    max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return int(max)
