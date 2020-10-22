#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/BinaryMatrix\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : A Binary matrix manipulation library  \n
Encoding    : UTF-8\n
Version     :0.7.17rc1\n
Build       :0.7.17rc1/29-08-2020
"""
#*-----------------------------------------------------------------------------*
# Imports
from pyrix.matrix import Matrix, matrixData
from pyrix.exception import binaryMatrixException,incompaitableTypeException
import random
import copy
#*-----------------------------------------------------------------------------*
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
    """
    A completely Innovative approach to Matrices with Binary numbers.
    Full Logic control with Matrix types.
    Can be used as comparators,Inverters,Bit Data Manipulators as a matrix.
    BinaryMatrix.__init__() :>
    """
    # Binary Matrix Methods

    def __init__(self, nrow=1, ncol=1, data=[1],mode='EBM',bit='1'):
        if(len(data) == nrow, len(data[0]) == ncol):
            self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)
            self.matrix.classType = 'BinaryMatrix'
            self.matrix.mode=mode
            setattr(self.matrix,'bitwidth',bit)
            self.isBinaryMatrix()

        else:
            raise incompaitableTypeException
    def __repr__(self):
        pass
    def __str__(self):
        stringV = str()
        stringV = "Binary Matrix ("
        stringV += str(self.matrix.mode)+" Mode) "+"Bit-Width :"+self.matrix.bitwidth+":\n"
        for item in self.matrix.data:
            stringV += str(item)+"\n"
        stringV += ("Dimensions :") + \
            str(self.matrix.dimensions[0])+"x"+str(self.matrix.dimensions[1])
        return stringV
    __repr__ = __str__

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(name)

    def __delattr__(self, name):
        del self.__dict__[name]

    def __add__(self, BinaryMat2):
        if(not BinaryMat2.isBinaryMatrix()):
            raise incompaitableTypeException
        sum = zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
        for i in range(0,self.matrix.nrow):
            for j in range(0,self.matrix.ncol):
                sum[i][j]=(self.matrix.data[i][j]+BinaryMat2.matrix.data[i][j])%2
        return sum
    def __sub__(self, BinaryMat2):
        if(not BinaryMat2.isBinaryMatrix()):
            raise incompaitableTypeException
        sum = zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
        for i in range(0, self.matrix.nrow):
            for j in range(0, self.matrix.ncol):
                sum[i][j]=(self.matrix.data[i][j]-BinaryMat2.matrix.data[i][j])%2
        return sum

    def __mul__(self, BinaryMat2):
        return super().__mul__(BinaryMat2)

    def __lshift__(self, bits):
        if(self.matrix.bitwidth==1):
            self.logicalShift(direction="left", bits=bits)

    def __rshift__(self, bits):
        if(self.matrix.bitwidth==1):
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
                            __AndS(self.matrix.data[i][j],
                                    m2.matrix.data[i][j])
                            )
                return BinaryMatrix(
                    nrow=self.matrix.nrow,
                    ncol=self.matrix.ncol,
                    data=data
                )
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
                            __Or(self.matrix.data[i][j],
                                    m2.matrix.data[i][j]))
                return BinaryMatrix(
                    nrow=self.matrix.nrow,
                    ncol=self.matrix.ncol,
                    data=data
                )
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
                            __Exor(self.matrix.data[i][j],
                                    m2.matrix.data[i][j]))
                return BinaryMatrix(
                    nrow=self.matrix.nrow,
                    ncol=self.matrix.ncol,
                    data=data
                )
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
            return BinaryMatrix(
                nrow=self.matrix.nrow,
                ncol=self.matrix.ncol,
                data=data
            )
        else:
            raise binaryMatrixException

    def onesComplement(self):
        return self.__invert__()

    def twosComplement(self):
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
        if(self.matrix.binaryMatrix == True) and (Bmatrix2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == Bmatrix2.matrix.dimensions):
                data = []
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            __Nand(self.matrix.data[i][j],
                                    Bmatrix2.matrix.data[i][j]))
                return BinaryMatrix(
                    nrow=self.matrix.nrow,
                    ncol=self.matrix.ncol,
                    data=data
                )
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
                            __Nor(self.matrix.data[i][j],
                                Bmatrix2.matrix.data[i][j]))
                return BinaryMatrix(
                    nrow=self.matrix.nrow,
                    ncol=self.matrix.ncol,
                    data=data
                )
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
                            __EXNor(self.matrix.data[i][j],
                                    Bmatrix2.matrix.data[i][j]))
                return BinaryMatrix(
                    nrow=self.matrix.nrow,
                    ncol=self.matrix.ncol,
                    data=data
                )
            else:
                raise incompaitableTypeException
        else:
            raise binaryMatrixException

    def logicalShift(self, direction, bits):
        dataArray = __listifyMatrix(self)
        right=["r","R","right","Right","RIGHT"]
        left=["l","L","left","Left","LEFT"]
        if direction in right:
            for _i in range(bits):
                dataArray.insert(0, 0)
                dataArray.pop()
        if direction in left:
            for _i in range(bits):
                dataArray.insert(-1, 0)
                dataArray.pop(0)
        setattr(self.matrix, name='data', value=dataArray)
        return self

    def circularShift(self, direction, bits):
        dataArray = __listifyMatrix(self)
        right=["r","R","right","Right","RIGHT"]
        left=["l","L","left","Left","LEFT"]
        if direction in right:
            for _i in range(bits):
                lastelement = dataArray[-1]
                dataArray.insert(0, lastelement)
                dataArray.pop()
        if direction in left:
            for _i in range(bits):
                firstelement = dataArray[0]
                dataArray.insert(-1, firstelement)
                dataArray.pop(0)
        setattr(self.matrix, name='data', value=dataArray)
        return self

    def arithmeticShift(self, direction, bits):
        dataArray = __listifyMatrix(self)
        right=["r","R","right","Right","RIGHT"]
        left=["l","L","left","Left","LEFT"]
        if direction in right:
            for _i in range(bits):
                MSBvalue = dataArray[0]
                dataArray.insert(0, MSBvalue)
                dataArray.pop()
        if direction in left:
            for _i in range(bits):
                LSBvalue = 0
                dataArray.insert(-1, LSBvalue)
                dataArray.pop(0)
        setattr(self.matrix, name='data', value=dataArray)
        return self

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


def zeroBinaryMatrix(nrow, ncol):
    """
    Create a zero Binary matrix of the given dimensions\n
    Retuns a BinaryMatrix Object
    """
    t = []
    for i in range(nrow):
        t.append([])
        for _j in range(ncol):
            t[i].append(0)
    return BinaryMatrix(
        nrow=nrow,
        ncol=ncol,
        data=t
    )

# unitBinaryMatrix
# Creates a Binary Matrix with ones of given size and shape


def unitBinaryMatrix(nrow, ncol):
    """
    Create a Unit Binary matrix of the given dimensions\n
    Retuns a BinaryMatrix Object
    """
    t = []
    for i in range(nrow):
        t.append([])
        for _j in range(ncol):
            t[i].append(1)
    return BinaryMatrix(
        nrow=nrow,
        ncol=ncol,
        data=t
    )
# identityBinaryMatrix
# Creates a Binarymatrix with zeros of given shape and size


def identityBinaryMatrix(nrow, ncol):
    """
    Create a identity Binary matrix of the given dimensions\n
    Works for square Matrices\n
    Retuns a BinaryMatrix Object
    """
    if(nrow == ncol):
        t = []
        for i in range(nrow):
            t.append([])
            for j in range(ncol):
                if(i == j):
                    t[i].append(1)
                else:
                    t[i].append(0)
        return BinaryMatrix(
            nrow=nrow,
            ncol=ncol,
            data=t
        )
    else:
        raise incompaitableTypeException


def randomBinaryMatrix(scale, type):
    if(scale == "small" and type == "int"):
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.randint(0, 1))
        return BinaryMatrix(
            nrow=nrow,
            ncol=ncol,
            data=data
        )
    if(scale == "large" and type == "int"):
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.randint(0, 1))
        return BinaryMatrix(
            nrow=nrow,
            ncol=ncol,
            data=data
        )

def Copy(AnyObject):
    return copy.deepcopy(AnyObject)
#*-----------------------------------------------------------------------------*
#*                          ░█▀█░█░█░█▀▄░▀█▀░█░█░
#*                          ░█▀▀░░█░░█▀▄░░█░░▄▀▄░
#*                          ░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░
#*-----------------------------------------------------------------------------*
