#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------ Brief Documentation --------------------
Name        : Pyrix/Vector\n
Author      : Abhishek Ulayil\n
Description : An extension to pyrix for vectors\n
Encoding    : UTF-8\n
Version     : 0.0.20
------------------------------------------------------------
"""
from Matrix import incompaitableTypeException, divisionErrorException, bitWiseOnMatrix

import copy


class vectorData:
    def __init__(self, dims, data):
        self.data = data
        self.dimensions = dims
        self.directionVectorSet = None
        self.ncol = dims

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            raise AttributeError(key)

    def __delattr__(self, key):
        del self.__dict__[key]


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

    def __mod__(self, m2):
        raise divisionErrorException

    def __lshift__(self, m2):
        raise bitWiseOnMatrix

    def __rshift__(self, m2):
        raise bitWiseOnMatrix

    def __and__(self, m2):
        raise bitWiseOnMatrix

    def __or__(self, m2):
        raise bitWiseOnMatrix

    def __xor__(self, m2):
        raise bitWiseOnMatrix

    def __invert__(self):
        raise bitWiseOnMatrix

    def copy(self):
        return copy.deepcopy(self)

    def dotProduct(self, v2):
        raise NotImplementedError

    def crossProduct(self, v2):
        raise NotImplementedError

    def orthogonalityVector(self):
        raise NotImplementedError

    def matrixMultiplication(self, m1):
        raise NotImplementedError


def unitVector(dims):
    VectorData = []
    for i in range(dims):
        VectorData.append([])
        VectorData[i].append(1)
    return Vector(dims=dims, data=VectorData)


def zeroVector(dims):
    VectorData = []
    for i in range(dims):
        VectorData.append([])
        VectorData[i].append(0)
    return Vector(dims=dims, data=VectorData)


def randomVector(scale, type):
    pass
