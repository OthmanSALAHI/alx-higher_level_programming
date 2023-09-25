#!/usr/bin/python3
def safe_print_integer(value):
    result = 0
    try:
        print("{:d}".format(value))
        return True
        result += 1
    except ValueError:
        return False
    return (result)
