#!/usr/bin/python3


class Square():

    def __init__(self, size=0):
        a = 0
        try:
            a += size
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")