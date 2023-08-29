#!/usr/bin/python3
""" define a Square """


class Square:
    """my Square"""
    def __init__(self, size=0):
        """init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""
        return self.__size ** 2

    @property
    def size(self):
        """Size Geter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size Seter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        def my_print(self):
            """my_print"""
            if not self.__size:
               print()
            return
        for i in range(self.__size):
            print("#" * self.__size)


