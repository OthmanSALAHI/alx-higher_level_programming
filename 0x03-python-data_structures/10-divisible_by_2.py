#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    boolean = []
    for i in range(length):
        if my_list[i] % 2 == 0:
            boolean.append(True)
        else:
            boolean.append(False)
    return boolean
