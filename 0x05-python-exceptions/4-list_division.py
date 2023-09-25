#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    res = 0
    for idx in range(list_length):
        try:
            res = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            res = 0
        except ValueError:
            res = 0
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return (new_list)
