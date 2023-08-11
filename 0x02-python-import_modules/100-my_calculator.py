#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import exit, argv
if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    c = ops[argv[2]](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, c))
