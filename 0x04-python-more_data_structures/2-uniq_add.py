#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    total = 0
    for num in new_list:
        total += num
    return total
