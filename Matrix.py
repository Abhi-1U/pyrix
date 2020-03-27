#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------ Brief Documentation --------------------
Author      : Abhishek Ulayil
Contents    : 2 Exceptions , 2 classes , 21 methods
Description : A simple matrix manipulation library  
Encoding    : UTF-8
Version     : 0.0.2
------------------------------------------------------------
"""
import sys


class divisionErrorException(Exception):
    pass


class incompaitableTypeException(Exception):
    pass


class matrixData(object):
    def __init__(self, **kwargs):
        self.dimensions = [kwargs['nrow'], kwargs['ncol']]
        self.__dict__['data'] = kwargs['data']
        self.__dict__['invertibility'] = None
        self.__dict__['determinant'] = None
        self.__dict__['singular'] = None
        self.__dict__['eigenvals'] = []
        self.__dict__['eigenvects'] = []
        self.__dict__['rank'] = None

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        return self.__dict__[key]

    def __delattr__(self, key):
        del self.__dict__[key]


class Matrix:

    def __init__(self, nrow=1, ncol=1, data=[1]):
        self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)

    def __str__(self):
        pass

    def __add__(self, *args):
        temp = []
        runcount = 0
        for matrix in args:
            for i in range(len(matrix.matrix.data)):
                temp.append([])
                print("added []")
                for j in range(len(matrix.matrix.data[i])):
                    if(runcount == 0):
                        temp[i].append(matrix.matrix.data[i][j])
                    else:
                        temp[i][j] += matrix.matrix.data[i][j]
            runcount += 1
        s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp)
        return s

    def __sub__(self, *args):
        temp = []
        runcount = 0
        for matrix in args:
            for i in range(len(matrix.matrix.data)):
                temp.append([])
                print("added []")
                for j in range(len(matrix.matrix.data[i])):
                    if(runcount == 0):
                        temp[i].append(matrix.matrix.data[i][j])
                    else:
                        temp[i][j] -= matrix.matrix.data[i][j]
            runcount += 1
        s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp)
        return s

    def __mul__(self, *args):
        pass

    def __div__(self, m2):
        raise divisionErrorException

    def __eq__(self, m2):
        pass

    def __floordiv__(self, m2):
        raise divisionErrorException

    def invertMatrix(self):
        pass

    def rowEchleonTransform(self):
        pass

    def RrowEchleonTransform(self):
        pass

    def copy(self):
        pass

    def transposeTransform(self):
        pass

    def vectorMultiplication(self, v1):
        pass

    def scaleMatrix(self):
        pass

    def determinantValue(self):
        pass

    def zeroMatrix(self, size):
        pass

    def identityMatrix(self, size):
        pass

    def matrixRank(self):
        pass

    def strassenMultiplication(self, m2):
        pass

    def eigenTerms(self):
        pass
