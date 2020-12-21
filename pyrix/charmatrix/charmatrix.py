#!/usr/bin/python3
# -*- coding : UTF-8 -*-

"""
Name        : Pyrix/CharactarMatrix\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : A Charactar matrix manipulation sub-library  \n
Encoding    : UTF-8\n
Version     :0.7.19\n
Build       :0.7.19/21-12-2020
"""

# *------- Imports ------------------------------------------------------------*

import copy
from pyrix.matrix import matrixData, Matrix
from pyrix.exception import (
    incompaitableTypeException,
    divisionErrorException,
    bitWiseOnMatrix,
)

# *----------------------------------------------------------------------------*

# *------- pyrix.charmatrix.CharMatrix ----------------------------------------*

class CharMatrix(Matrix):
    """
    Charactar Matrix is a Matrix of charactars spanned out with some
    special functionality to easily manage such arrays/matrix of charactars.
    """
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

    #*------- Divide CharMatrix -----------------------------------------------*

    def __truediv__(self, m2):
        raise divisionErrorException("Can Matrices be divided ?")

    #*------- FloorDivide CharMatrix ------------------------------------------*

    def __floordiv__(self, m2):
        raise divisionErrorException

    #*------- Modulus CharMatrix ----------------------------------------------*

    def __mod__(self, m2):
        raise divisionErrorException

    #*------- lshift << CharMatrix --------------------------------------------*

    def __lshift__(self, m2):
        raise bitWiseOnMatrix

    #*------- rshift >> CharMatrix --------------------------------------------*

    def __rshift__(self, m2):
        raise bitWiseOnMatrix

    #*------- AND & CharMatrix ------------------------------------------------*

    def __and__(self, m2):
        raise bitWiseOnMatrix

    #*------- OR | CharMatrix -------------------------------------------------*

    def __or__(self, m2):
        raise bitWiseOnMatrix

    #*------- XOR ^ CharMatrix ------------------------------------------------*

    def __xor__(self, m2):
        raise bitWiseOnMatrix

    #*------- INVERT ~ CharMatrix ---------------------------------------------*

    def __invert__(self):
        raise bitWiseOnMatrix

    #*------- pyrix.charmatrix.CharMatrix.copy() ------------------------------*

    def copy(self):
        """
        Returns A Deep copy of the object
        """
        return copy.deepcopy(self)

    #*------- pyrix.charmatrix.CharMatrix.isSquareMatrix() --------------------*

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

    #*------- pyrix.charmatrix.CharMatrix.getRow() ----------------------------*

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

    #*------- pyrix.charmatrix.CharMatrix.getCol() ----------------------------*

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

    #*------- pyrix.charmatrix.CharMatrix.transposeTransform() ----------------*

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

    #*------- pyrix.charmatrix.CharMatrix.findCharactar() ---------------------*

    def findCharactar(self, charactar):
        """
        This method will return the given charactars location if it exists else 
        None.
        """
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                if charactar == self.matrix.data[i][j]:
                    return [i, j]

    #*------- pyrix.charmatrix.CharMatrix.ASCIIvals() -------------------------*

    def ASCIIvals(self):
        """
        Generates a Matrix object with ASCII values of the current CharMatrix.
        """
        data = self.copy().matrix.data
        returndata = []
        for i in range(self.matrix.nrow):
            returndata.append([])
            for j in range(self.matrix.ncol):
                returndata[i].append(ord(data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=returndata)

# *------- pyrix.charmatrix.alphaMatrix5x5() ----------------------------------*

def alphaMatrix5x5(offsetchars=[]):
    """
    This method will return a matrix with all alphabets repeated once, i/j 
    considered as a single element and 25 charactars spread out in 5x5 grid.
    """
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

# *------- pyrix.charmatrix.__nestifyMatrix() ---------------------------------*

def __nestifyMatrix(listeddata, rowcount, colcount):
    clist = listeddata
    nested = []
    for _i in range(rowcount):
        nested.append(clist[0:colcount])
        del clist[0:colcount]
    return nested
