#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            result += 1
        except ValueError as e:
            print("Error of {}".format(e))
    print()
    return (result)

