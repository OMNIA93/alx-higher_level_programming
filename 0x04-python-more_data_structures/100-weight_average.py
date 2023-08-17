#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    n = 0
    avg = 0
    for i in my_list:
        avg += i[0] * i[1]
        n += i[1]
    return avg / n
