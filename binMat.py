#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Name        : Pyrix/BinaryMatrix\n
Author      : Abhishek Ulayil\n
Description : A Binary matrix manipulation library  \n
Encoding    : UTF-8\n
--------------------------------------------------------------------
"""
from Matrix import Matrix, matrixData, incompaitableTypeException
from PyrixExceptions import binaryMatrixException
"""
Unique methods List:
1. binary add
2. binary subtract
3. isBinaryMatrix
4. boolean/logical and
5. boolean/logical or
6. boolean/logical invert
7. boolean/logical xor
8. bitwise lshift
9. bitwise rshift
10. boolean/logical Nand
11. boolean/logical Nor
12. UnitBinaryMatrix
13. ZeroBinaryMatrix
14. IdentityBinaryMatrix
15. RandmBinaryMatrix
16. listifymatrix
17. reDimensionalizeMatrix
18. flipDimensions
19. JSON import/export
20. onesComplement
21. twosComplement
22. boolean/logical ExNor
"""


class BinaryMatrix(Matrix):
    """A completely Innovative approach to Matrices with Binary numbers.\n
        Full Logic control with Matrix types.\n
        Can be used as comparators,Inverters,Bit Data Manipulators as a matrix.
    """
    # Binary Matrix Methods

    def __init__(self, nrow=1, ncol=1, data=[1]):
        if(len(data) == nrow, len(data[0]) == ncol):
            self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)
            self.matrix.classType = 'BinaryMatrix'
            self.isBinaryMatrix()
        else:
            raise incompaitableTypeException

    def __str__(self):
        stringV = str()
        stringV = "Binary Matrix:\n"
        for item in self.matrix.data:
            stringV += str(item)+"\n"
        stringV += ("Dimensions :") + \
            str(self.matrix.dimensions[0])+"x"+str(self.matrix.dimensions[1])
        return stringV

    def __add__(self, BinaryMat2):
        carryterm = 0
        if(not BinaryMat2.isBinaryMatrix()):
            raise incompaitableTypeException
        sum = __zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
        for i in range(self.matrix.nrow-1, -1, -1):
            for j in range(self.matrix.ncol-1, -1, -1):
                localsum = (
                    self.matrix.data[i][j]+BinaryMat2.matrix.data[i][j]+carryterm)
                if(localsum == 0):
                    sum.matrix.data[i][j] = 0
                    continue
                if(localsum == 1):
                    sum.matrix.data[i][j] = 1
                    continue
                if(localsum == 2):
                    carryterm = 1
                    sum.matrix.data[i][j] = 0
                    continue
                if(localsum == 3):
                    carryterm = 1
                    sum.matrix.data[i][j] = 1
                    continue
        return sum

    def __sub__(self, BinaryMat2):
        carryterm = 0
        if(not BinaryMat2.isBinaryMatrix()):
            raise incompaitableTypeException
        sum = __zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
        for i in range(self.matrix.nrow-1, -1, -1):
            for j in range(self.matrix.ncol-1, -1, -1):
                localsum = (
                    self.matrix.data[i][j]-BinaryMat2.matrix.data[i][j]+carryterm)
                if(localsum == 0):
                    sum.matrix.data[i][j] = 0
                    continue
                if(localsum == 1):
                    sum.matrix.data[i][j] = 1
                    continue
                if(localsum == -1):
                    carryterm = -1
                    sum.matrix.data[i][j] = 1
                    continue
                if(localsum == -2):
                    carryterm = 1
                    sum.matrix.data[i][j] = 0
                    continue
        return sum

    def __mul__(self, BinaryMat2):
        print("Multiplication on binary Matrices will Change the complete structure and make it impossibly wierd to represent.")

    def __lshift__(self, bits):
        self.logicalShift(direction="left", bits=bits)

    def __rshift__(self, bits):
        self.logicalShift(direction="Right", bits=bits)

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
                            __AndS(self.matrix.data[i][j], m2.matrix.data[i][j]))
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
                            __Or(self.matrix.data[i][j], m2.matrix.data[i][j]))
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
                            __Exor(self.matrix.data[i][j], m2.matrix.data[i][j]))
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
                        __Not(self.matrix.data[i][j]))
            return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
        else:
            raise binaryMatrixException

    def onesComplement(self):
        return self.__invert__()

    def twosSomplement(self):
        binaryinvertedmatrix = self.onesComplement()
        lastrow = binaryinvertedmatrix.matrix.nrow
        lastcol = binaryinvertedmatrix.matrix.ncol
        lastelement = binaryinvertedmatrix.matrix.data[lastrow-1][lastcol-1]
        if(lastelement == 0):
            lastelement += 1
        else:
            data = self.__forward_one(data=binaryinvertedmatrix.matrix.data,
                                      rowcount=lastrow, colcount=lastcol)
            binaryinvertedmatrix.matrix.data = data
        return binaryinvertedmatrix

    def __forward_one(self, data, rowcount, colcount):
        for _i in range(rowcount-1, 0, -1):
            for _j in range(colcount-1, 0, -1):
                if(data[_i][_j] == 1):
                    data[_i][_j] == 0
                    continue
                if(data[_i][_j] == 0):
                    data[_i][_j] == 1
        return data

    def Nand(self, Bmatrix2):
        self.isBinaryMatrix()
        Bmatrix2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and Bmatrix2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == Bmatrix2.matrix.dimensions):
                data = []
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            __Nand(self.matrix.data[i][j], Bmatrix2.matrix.data[i][j]))
                return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
            else:
                raise incompaitableTypeException
        else:
            raise binaryMatrixException

    def Nor(self, Bmatrix2):
        self.isBinaryMatrix()
        Bmatrix2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and Bmatrix2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == Bmatrix2.matrix.dimensions):
                data = []
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            __Nor(self.matrix.data[i][j], Bmatrix2.matrix.data[i][j]))
                return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
            else:
                raise incompaitableTypeException
        else:
            raise binaryMatrixException

    def ExNor(self, Bmatrix2):
        self.isBinaryMatrix()
        Bmatrix2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and Bmatrix2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == Bmatrix2.matrix.dimensions):
                data = []
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            __EXNor(self.matrix.data[i][j], Bmatrix2.matrix.data[i][j]))
                return BinaryMatrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=data)
            else:
                raise incompaitableTypeException
        else:
            raise binaryMatrixException

    def logicalShift(self, direction, bits):
        dataArray = __listifyMatrix(self)
        if (direction == "r") or (direction == "R") or (direction == "right") or (direction == "Right") or (direction == "RIGHT"):
            for _i in range(bits):
                dataArray.insert(0, 0)
                dataArray.pop()
        if (direction == "l") or (direction == "L") or (direction == "left") or (direction == "Left") or (direction == "LEFT"):
            for _i in range(bits):
                dataArray.insert(-1, 0)
                dataArray.pop(0)
        setattr(self.matrix, name='data', value=dataArray)

    def circularShift(self, direction, bits):
        dataArray = __listifyMatrix(self)
        if (direction == "r") or (direction == "R") or (direction == "right") or (direction == "Right") or (direction == "RIGHT"):
            for _i in range(bits):
                lastelement = dataArray[-1]
                dataArray.insert(0, lastelement)
                dataArray.pop()
        if (direction == "l") or (direction == "L") or (direction == "left") or (direction == "Left") or (direction == "LEFT"):
            for _i in range(bits):
                firstelement = dataArray[0]
                dataArray.insert(-1, firstelement)
                dataArray.pop(0)
        setattr(self.matrix, name='data', value=dataArray)

    def arithmeticShift(self, direction, bits):
        dataArray = __listifyMatrix(self)
        if (direction == "r") or (direction == "R") or (direction == "right") or (direction == "Right") or (direction == "RIGHT"):
            for _i in range(bits):
                MSBvalue = dataArray[0]
                dataArray.insert(0, MSBvalue)
                dataArray.pop()
        if (direction == "l") or (direction == "L") or (direction == "left") or (direction == "Left") or (direction == "LEFT"):
            for _i in range(bits):
                LSBvalue = 0
                dataArray.insert(-1, LSBvalue)
                dataArray.pop(0)
        setattr(self.matrix, name='data', value=dataArray)

    def popcount(self):
        popcount = 0
        dataArray = __listifyMatrix(self)
        for value in dataArray:
            if (value != 0):
                popcount += 1
            else:
                continue
        return popcount


def __Exor(t1, t2):
    if(t1 == t2):
        return 0
    else:
        return 1


def __AndS(t1, t2):
    if(t1 == t2 == 1):
        return 1
    else:
        return 0


def __Or(t1, t2):
    if(t1 == t2 == 0):
        return 0
    else:
        return 1


def __Not(t1):
    if(t1 == 1):
        return 0
    else:
        return 1


def __Nand(t1, t2):
    if(t1 == t2 == 1):
        return 0
    else:
        return 1


def __Nor(t1, t2):
    if(t1 == t2 == 0):
        return 1
    else:
        return 0


def __EXNor(t1, t2):
    if(t1 == t2):
        return 1
    else:
        return 0


def __listifyMatrix(BinaryMatrixObject):
    matrixdata = BinaryMatrixObject.matrix.data
    listifiedmatrix = []
    for i in range(BinaryMatrixObject.matrix.nrow):
        for j in range(BinaryMatrixObject.matrix.ncol):
            listifiedmatrix.append(matrixdata[i][j])
    BinaryMatrixObject.matrix.listifieddata = listifiedmatrix
    return listifiedmatrix


def __zeroBinaryMatrix(nrow, ncol):
    """Create a zero Binary matrix of the given dimensions\n
        Retuns a BinaryMatrix Object
    """
    t = []
    for i in range(nrow):
        t.append([])
        for _j in range(ncol):
            t[i].append(0)
    s = BinaryMatrix(nrow=nrow, ncol=ncol, data=t)
    return s
