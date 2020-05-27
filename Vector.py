#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------ Brief Documentation --------------------
Name        : Pyrix/Vector\n
Author      : Abhishek Ulayil\n
Description : An extension to pyrix for vectors\n
Encoding    : UTF-8
------------------------------------------------------------
"""
from PyrixExceptions import incompaitableTypeException, divisionErrorException, bitWiseOnMatrix
import math
import copy

# Vector is treated like a List
# Unlike Matrix which is Nested List


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
        stringV = str()
        stringV = "Vector:\n"
        for item in self.vector.data:
            stringV += str(item)+"\n"
        stringV += "Dimensions :" + \
            str(self.vector.dimensions)
        return stringV

    def __repr__(self):
        pass

    def __add__(self, Vector2):
        if(self.vector.dimensions == Vector2.vector.dimensions):
            sum = []
            for i in range(self.vector.dimensions):
                sum.append(self.vector.data[i]+Vector2.vector.data[i])
            return Vector(dims=self.vector.dimensions, data=sum)
        else:
            raise incompaitableTypeException

    def __sub__(self, Vector2):
        if(self.vector.dimensions == Vector2.vector.dimensions):
            diff = []
            for i in range(self.vector.dimensions):
                diff.append(self.vector.data[i]-Vector2.vector.data[i])
            return Vector(dims=self.vector.dimensions, data=diff)
        else:
            raise incompaitableTypeException

    def __mul__(self, *args):
        pass

    def __truediv__(self, m2):
        raise divisionErrorException

    def __eq__(self, vector2):
        if(self.vector.dimensions == vector2.vector.dimensions)and (self.vector.data == vector2.vector.data):
            return True
        else:
            return False

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

    def __abs__(self):
        return self.vectorNorm()

    def __pow__(self):
        return self.dotProduct(v2=self)

    def copy(self):
        return copy.deepcopy(self)

    def dotProduct(self, v2):
        assert self.vector.dimensions == v2.vector.dimensions, "incompaitableTypeException"
        dotproduct = 0
        for i in range(self.vector.dimensions):
            dotproduct += (self.vector.data[i])*(v2.vector.data[i])
        return dotproduct

    def vectorNorm(self):
        norm = math.sqrt(self.dotProduct(v2=self))
        return norm

    def vectorNormalize(self):
        normValue = self.vectorNorm()
        assert (normValue != 0), "Vector normal value 0"
        for i in range(self.vector.dimensions):
            self.vector.data[i] /= normValue
        return self

    def scaleVector(self, scalar):
        data = self.vector.data
        for i in range(self.vector.dimensions):
            data[i] *= scalar
        return self

    def crossProduct(self, v2):
        raise NotImplementedError

    def orthogonalityVector(self):
        raise NotImplementedError


def unitVector(dims):
    VectorData = []
    for _i in range(dims):
        VectorData.append(1)
    return Vector(dims=dims, data=VectorData)


def zeroVector(dims):
    VectorData = []
    for _i in range(dims):
        VectorData.append(0)
    return Vector(dims=dims, data=VectorData)


def randomVector(scale, type):
    pass


def linearVector(dims, minVal, maxVal):
    assert minVal <= maxVal
    'Not suitable Range'
    assert dims > 1
    'Dimensions too small'
    data = []
    gap = (maxVal-minVal)/(dims-1)
    for i in range(dims):
        data.append(minVal+gap*i)
    linVector = Vector(dims=dims, data=data)
    return linVector
