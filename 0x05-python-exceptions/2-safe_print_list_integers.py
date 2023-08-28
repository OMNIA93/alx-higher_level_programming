#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
printed_list = 0
for idx in rang(x):
printed_list += 1
try
print "{:d}".format(my_list[idx]), end="")
except (ValueError, TypeError):
printed_list -= 1
print()
return printed_list
