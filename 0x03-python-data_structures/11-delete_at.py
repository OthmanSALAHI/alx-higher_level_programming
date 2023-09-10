#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newlist = list(my_list)
    if idx > len(my_list) or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
