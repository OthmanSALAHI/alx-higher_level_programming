#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return newlist
    else:
        newlist[idx] = element
        return newlist
