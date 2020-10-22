#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/CharactarMatrix\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : A Charactar matrix manipulation sub-library  \n
Encoding    : UTF-8\n
Version     :0.7.17rc1\n
Build       :0.7.17rc1/22-10-2020
"""
import copy
from pyrix.matrix import matrixData, Matrix
from pyrix.exception import (
    incompaitableTypeException,
    divisionErrorException,
    bitWiseOnMatrix,
)


class CharMatrix(Matrix):
    def __init__(self, nrow=1, ncol=1, data=[[""]]):
        if (len(data) == nrow, len(data[0]) == ncol):
            self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)
            self.matrix.classType = "CharactarMatrix"
        else:
            raise incompaitableTypeException

    def __repr__(self):
        pass

    def __str__(self):
        stringV = str()
        stringV = "Charactar Matrix:\n"
        for item in self.matrix.data:
            stringV += str(item) + "\n"
        stringV += (
            "Dimensions :"
            + str(self.matrix.dimensions[0])
            + "x"
            + str(self.matrix.dimensions[1])
        )
        return stringV

    __repr__ = __str__
    # 4. Divide Matrix
    # A method just to avoid division by operator

    def __truediv__(self, m2):
        raise divisionErrorException("Can Matrices be divided ?")

    # 5. Divide Matrix
    # A method just to avoid floor division by operator
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

    def isSquareMatrix(self):
        """
        Checks if the Matrix is a square Matrix or not\n
        A square matrix is a matrix with equal number of rows and cols\n
        Returns a Boolean value
        """
        if self.matrix.nrow == self.matrix.ncol:
            return True
        else:
            return False

    def getRow(self, index):
        """
        Selects a Row of the matrix of specified index\n
        Returns a list of the values
        """
        temp = [[]]
        for j in range(self.matrix.ncol):
            temp[0].append(self.matrix.data[index][j])
        s = CharMatrix(nrow=1, ncol=self.matrix.ncol, data=temp)
        return s

    # 11. getcol
    # returns a specified column

    def getCol(self, index):
        """
        Selects a Column of the matrix of specified index\n
        Returns a list(or nested list) of the values
        """
        temp = []
        for i in range(self.matrix.nrow):
            temp.append([])
            temp[i].append(self.matrix.data[i][index])
        s = CharMatrix(nrow=self.matrix.nrow, ncol=1, data=temp)
        return s

    def transposeTransform(self):
        """
        Transpose of the original matrix is created.\n
        Returns a Matrix Object.
        """
        c = []
        for i in range(self.matrix.ncol):
            c.append([])
            for j in range(self.matrix.nrow):
                c[i].append(self.matrix.data[j][i])
        s = CharMatrix(nrow=self.matrix.ncol, ncol=self.matrix.nrow, data=c)
        return s

    def findCharactar(self, charactar):
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                if charactar == self.matrix.data[i][j]:
                    return [i, j]

    def ASCIIvals(self):
        data = self.copy().matrix.data
        returndata = []
        for i in range(self.matrix.nrow):
            returndata.append([])
            for j in range(self.matrix.ncol):
                returndata[i].append(ord(data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=returndata)


def alphaMatrix5x5(offsetchars=[]):
    table = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if len(offsetchars) != 0:
        for i in offsetchars:
            assert i.isalpha(), "Key should contain only alphabets"
            if i in table:
                continue
            if i == "j":
                if "i" in table:
                    continue
                else:
                    table.append("i")
                continue
            else:
                table.append(i)
    for i in range(len(alpha)):
        if alpha[i] in table:
            continue
        if alpha[i] == "j":
            if "i" in table:
                continue
            else:
                table.append("i")
            continue
        else:
            table.append(alpha[i])
    outmatrix = CharMatrix(nrow=5, ncol=5, data=__nestifyMatrix(table, 5, 5))
    return outmatrix

def __nestifyMatrix(listeddata, rowcount, colcount):
    clist = listeddata
    nested = []
    for _i in range(rowcount):
        nested.append(clist[0:colcount])
        del clist[0:colcount]
    return nested


# *-----------------------------------------------------------------------------*
# *                          ░█▀█░█░█░█▀▄░▀█▀░█░█░
# *                          ░█▀▀░░█░░█▀▄░░█░░▄▀▄░
# *                          ░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░
# *-----------------------------------------------------------------------------*
