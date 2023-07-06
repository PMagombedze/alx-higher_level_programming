#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """returns new matrix, matrix divided by div"""
    len_ = None
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for n in matrix:
        if type(n) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len_ is None:
            len_ = len(n)
        elif len_ != len(n):
            raise TypeError("Ëach row of the matrix must have the same size")
        for i in n:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (lits of lists) of integers/matrix")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    c = round(i / div, 2)
    return [[c for i in n] for n in matrix]
