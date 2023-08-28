#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
m = 0
    for i in range(x):
        m += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            m -= 1
    print()
    return m
