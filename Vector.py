#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------ Brief Documentation --------------------
Author      : Abhishek Ulayil
Contents    : 3 Exceptions , 2 classes , 25 methods
Description : An extension to pyrix for vectors
Encoding    : UTF-8
Version     : 0.0.12
------------------------------------------------------------
"""
from Matrix import incompaitableTypeException, divisionErrorException


class vectorData:
    def __init__(self, dims, data):
        self.data = data
        self.dimensions = dims
        self.directionVectorSet = None


class Vector:
    def __init__(self, dims, data):
        self.vector = vectorData(dims, data)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __add__(self, *args):
        pass

    def __sub__(self, *args):
        pass

    def __mul__(self, *args):
        pass

    def __truediv__(self, m2):
        raise divisionErrorException

    def __eq__(self, m2):
        pass

    def __floordiv__(self, m2):
        raise divisionErrorException

    def copy(self):
        pass

    def dotProduct(self, v2):
        raise NotImplementedError

    def crossProduct(self, v2):
        raise NotImplementedError

    def orthogonalityVector(self):
        raise NotImplementedError

    def matrixMultiplication(self, m1):
        raise NotImplementedError


def unitVector(dims):
    pass


def zeroVector(dims):
    pass
