#!/usr/bin/python3
def no_c(my_string):
    modified_string = ""
    for char in my_string:
        if char != 'C' and char != 'c':
            modified_string += char
    return modified_string
