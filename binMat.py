#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Name        : Pyrix/BinaryMatrix\n
Author      : Abhishek Ulayil\n
Contents    : 2 Exceptions Classes , 1 Function classes , 10 methods\n
Description : A Binary matrix manipulation library  \n
Encoding    : UTF-8\n
Version     : 0.0.30
--------------------------------------------------------------------
"""
from Matrix import Matrix, matrixData, incompaitableTypeException, binaryMatrixException, nestifyMatrix
import random
import json
from filepath import fileChooserUI, folderChooserUI
"""
Unique methods List:
1. binary add
2. binary subtract
3. isBinaryMatrix
4. boolean and
5. boolean or
6. boolean invert
7. boolean xor
8. bitwise lshift
9. bitwise rshift
1
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
        sum = zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
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
        sum = zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
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
        pass

    def __rshift__(self, bits):
        pass

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

    def onesComplement(self):
        pass


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


def Nand(t1, t2):
    pass


def Nor(t1, t2):
    pass


def zeroBinaryMatrix(nrow, ncol):
    """Create a zero Binary matrix of the given dimensions\n
        Retuns a BinaryMatrix Object
    """
    t = []
    for i in range(nrow):
        t.append([])
        for j in range(ncol):
            t[i].append(0)
    s = BinaryMatrix(nrow=nrow, ncol=ncol, data=t)
    return s

# unitBinaryMatrix
# Creates a Binary Matrix with ones of given size and shape


def unitBinaryMatrix(nrow, ncol):
    """Create a Unit Binary matrix of the given dimensions\n
        Retuns a BinaryMatrix Object
    """
    t = []
    for i in range(nrow):
        t.append([])
        for j in range(ncol):
            t[i].append(1)
    s = BinaryMatrix(nrow=nrow, ncol=ncol, data=t)
    return s
# identityBinaryMatrix
# Creates a Binarymatrix with zeros of given shape and size


def identityBinaryMatrix(nrow, ncol):
    """Create a identity Binary matrix of the given dimensions\n
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
        s = BinaryMatrix(nrow=nrow, ncol=ncol, data=t)
        return s
    else:
        raise incompaitableTypeException


def randomMatrix(scale, type):
    if(scale == "small" and type == "int"):
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for j in range(ncol):
                data[i].append(random.randint(0, 1))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if(scale == "large" and type == "int"):
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for j in range(ncol):
                data[i].append(random.randint(0, 1))
        s = BinaryMatrix(nrow=nrow, ncol=ncol, data=data)
        return s


def listifyMatrix(BinaryMatrixObject):
    matrixdata = BinaryMatrixObject.matrix.data
    listifiedmatrix = []
    for i in range(BinaryMatrixObject.matrix.nrow):
        for j in range(BinaryMatrixObject.matrix.ncol):
            listifiedmatrix.append(matrixdata[i][j])
    BinaryMatrixObject.matrix.listifieddata = listifiedmatrix
    return listifiedmatrix


def reDimensionalize(BinaryMatrixObject, nrow, ncol):
    listifieddata = listifyMatrix(BinaryMatrixObject)
    matrixdata = []
    for i in range(nrow):
        matrixdata.append([])
        matrixdata[i] = listifieddata[0:ncol]
        del listifieddata[0:ncol]
    return BinaryMatrix(nrow=nrow, ncol=ncol, data=matrixdata)


def switchAxis(BinaryMatrixObject):
    newcol = BinaryMatrixObject.matrix.nrow
    newrow = BinaryMatrixObject.matrix.ncol
    return reDimensionalize(BinaryMatrixObject, newrow, newcol)


def JSONEncoder(object):
    Object = object
    return Object.matrix.__dict__


def JSONExport(Object, filename):
    data = JSONEncoder(Object)
    with open(filename, "w") as outfile:
        json.dump(data, outfile)
        outfile.close()
    print("Export Of Object Data Successfull!")


def JSONDecoder(object):
    classtype = None
    nrow = 0
    ncol = 0
    data = []
    for key, item in object.items():
        if(key == 'classType'):
            classtype = item
            continue
        if(key == 'nrow'):
            nrow = item
            continue
        if(key == 'ncol'):
            ncol = item
            continue
        if(key == 'data'):
            data = item
            break
    if classtype == 'BinaryMatrix':
        returnMatrix = BinaryMatrix(nrow=nrow, ncol=ncol, data=data)
        for key, item in object.items():
            setattr(returnMatrix.matrix, key, item)
    if classtype == 'Matrix':
        returnMatrix = Matrix(nrow=nrow, ncol=ncol, data=data)
        for key, item in object.items():
            setattr(returnMatrix.matrix, key, item)
    return returnMatrix


def JSONImport(filename, mode="UI"):
    if(mode == "UI"):
        filepath = fileChooserUI()
    else:
        filepath = filename
    with open(filepath, 'r') as openfile:
        json_object = json.load(openfile)
        openfile.close()
    return JSONDecoder(json_object)
