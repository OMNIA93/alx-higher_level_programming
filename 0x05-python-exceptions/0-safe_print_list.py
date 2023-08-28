#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    print_length_elements = 0

    for idx in range(x):
        try:
            print('{}'.format(my_list[idx]), end="")
            print_length_elements += 1
        except IndexError:
            pass

    print("")
    return print_length_elements
