#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
print_number_elements = 0
for i in range(x):
try:
print(my_list[i], end='')
print_number_elements += 1
except IndexError:
pass
print()
return print_number_elements
