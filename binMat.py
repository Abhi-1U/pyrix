#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Name        : Pyrix/BinaryMatrix\n
Author      : Abhishek Ulayil\n
Contents    : 2 Exceptions Classes , 1 Function classes , 10 methods\n
Description : A Binary matrix manipulation library  \n
Encoding    : UTF-8\n
Version     : 0.0.3
--------------------------------------------------------------------
"""
from Matrix import Matrix, matrixData, incompaitableTypeException, binaryMatrixException


class BinaryMatrix(Matrix):
    """A completely Innovative approach to Matrices with Binary numbers.\n
        Full Logic control with Matrix types.\n
        Can be used as comparators,Inverters,Bit Data Manipulators as a matrix.
    """
    # Binary Matrix Methods

    def __init__(self, nrow=1, ncol=1, data=[1]):
        if(len(data) == nrow, len(data[0]) == ncol):
            self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)
            self.isBinaryMatrix()
        else:
            raise incompaitableTypeException

    def __str__(self):
        stringV = str()
        stringV = "Binary Matrix:\n"
        for item in self.matrix.data:
            stringV += str(item)+"\n"
        stringV += "Dimensions :" + \
            str(self.matrix.dimensions[0])+"x"+str(self.matrix.dimensions[1])
        return stringV

    def isBinaryMatrix(self):
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                if(self.matrix.data[i][j] == 1):
                    continue
                if(self.matrix.data[i][j] == 0):
                    continue
                else:
                    self.matrix.binaryMatrix = False
                    raise binaryMatrixException
        self.matrix.binaryMatrix = True
        return self.matrix.binaryMatrix

    def __and__(self, m2):
        self.isBinaryMatrix()
        m2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and m2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == m2.matrix.dimensions):
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            AndS(self.matrix.data[i][j], m2.matrix.data[i][j]))
                return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
            else:
                raise incompaitableTypeException
        else:
            raise binaryMatrixException

    def __or__(self, m2):
        self.isBinaryMatrix()
        m2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and m2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == m2.matrix.dimensions):
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            Or(self.matrix.data[i][j], m2.matrix.data[i][j]))
                return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
            else:
                raise incompaitableTypeException
        else:
            raise binaryMatrixException

    def __xor__(self, m2):
        self.isBinaryMatrix()
        m2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and m2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == m2.matrix.dimensions):
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            Exor(self.matrix.data[i][j], m2.matrix.data[i][j]))
                return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
            else:
                raise incompaitableTypeException
        else:
            raise binaryMatrixException

    def __invert__(self):
        self.isBinaryMatrix()

        if(self.matrix.binaryMatrix == True):
            data = []
            for i in range(self.matrix.nrow):
                data.append([])
                for j in range(self.matrix.ncol):
                    data[i].append(
                        Not(self.matrix.data[i][j]))
            return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
        else:
            raise binaryMatrixException


def Exor(t1, t2):
    if(t1 == t2):
        return 0
    else:
        return 1


def AndS(t1, t2):
    if(t1 == t2 == 1):
        return 1
    else:
        return 0


def Or(t1, t2):
    if(t1 == t2 == 0):
        return 0
    else:
        return 1


def Not(t1):
    if(t1 == 1):
        return 0
    else:
        return 1
