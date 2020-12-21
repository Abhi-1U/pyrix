#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/Exceptions\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : Exceptions are implemented here  \n
Encoding    : UTF-8\n
Version     :0.7.19\n
Build       :0.7.19/21-12-2020
"""


class ExceptionTemplate(Exception):
    def __call__(self, *args):
        return self.__class__(*(self.args + args))

    def __str__(self):
        return ": ".join(self.args)


class bitWiseOnMatrix(ExceptionTemplate):
    """
    Traditional Bitwise Operators are not allowed to work on matrix objects as
    of now.\n Maybe in future we will find a creative use case of them.
    """


class binaryMatrixException(ExceptionTemplate):
    """
    Not a Binary Matrix
    """


class divisionErrorException(ExceptionTemplate):
    """
    Can Matrices be Divided ?
    """


class incompaitableTypeException(Exception):
    """
    If you come across this Exception then the issue is probably out of these
    four cases:\n
    Case 1: The dimensions of matrices dont match for the operation to happen\n
    Case 2: The matrix is not a square matrix\n
    Case 3: The matrices do not satisfy the condition for multiplication\n
    Case 4: The Data of the Matrix is not of the Dimensions Given.
    """


class nonInvertibleException(Exception):
    """
    Matrix is not invertible due to its singular nature and determinant being
    zero.
    """