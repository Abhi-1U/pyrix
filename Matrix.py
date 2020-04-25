#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Author      : Abhishek Ulayil
Contents    : 4 Exceptions Classes , 2 Function classes , 43 methods
Description : A simple matrix manipulation library  
Encoding    : UTF-8
Version     : 0.8.75
--------------------------------------------------------------------
"""
import sys
import copy
import functools
import argparse
import os


class ExceptionTemplate(Exception):
    def __call__(self, *args):
        return self.__class__(*(self.args + args))

    def __str__(self):
        return ': '.join(self.args)


class divisionErrorException(ExceptionTemplate):
    """Can Matrices be Divided ?"""


class incompaitableTypeException(Exception):
    """If you come across this Exception then the issue is probably out of these three cases:
        Case 1: The dimensions of matrices dont match for the operation to happen
        Case 2: The matrix is not a square matrix
        Case 3: The matrices do not satisfy the condition for multiplication 
    """


class nonInvertibleException(Exception):
    """Matrix is not invertible due to its singular nature and determinant being zero"""


class matrixData(object):
    def __init__(self, nrow, ncol, data):
        self.nrow = nrow
        self.ncol = ncol
        self.dimensions = [nrow, ncol]
        self.data = data
        self.invertibility = None
        self.determinant = None
        self.singular = None
        self.eigenvals = []
        self.eigenvects = []
        self.rank = None

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            raise AttributeError(key)

    def __delattr__(self, key):
        del self.__dict__[key]


""" 
Function List
1. Initialization Matrix
2. Add/Subtract/Multiply
3. Equality Check
4. Inversion
5. Add_row,Sub_row,Multiply_row,getrow,getcol
6. RowEchleonTransform
7. Copy
8. Transpose
9. determinant
10. Vector Multiplication
11. scale 
12. Strassen Multiplication
13. Identity Matrix
14. zero Matrix
15. isSquareMatrix
16. isInvertible
17. RoundOff
18. Rank
19. ReducedRowEchleonTransform
"""


class Matrix:

    def __init__(self, nrow=1, ncol=1, data=[1]):
        self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)

    def __repr__(self):
        pass

    def __str__(self):
        stringV = str()
        stringV = "Matrix:\n"
        for item in self.matrix.data:
            stringV += str(item)+"\n"
        stringV += "Dimensions :" + \
            str(self.matrix.dimensions[0])+"x"+str(self.matrix.dimensions[1])
        return stringV

# Basic Operations on Matrices
# 1. Add Matrix
# Operator Overloading for adding Matrices

    def __add__(self, m2):
        if(self.matrix.dimensions != m2.matrix.dimensions):
            raise incompaitableTypeException
        else:
            temp = self.matrix.data
            for i in range(len(m2.matrix.data)):
                for j in range(len(m2.matrix.data[i])):
                    temp[i][j] += m2.matrix.data[i][j]
            s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp)
            return s

# 2. Subtract Matrix
# Operator Overloading for subtracting Matrices

    def __sub__(self, m2):
        if(self.matrix.dimensions != m2.matrix.dimensions):
            raise incompaitableTypeException
        else:
            temp = self.matrix.data
            for i in range(len(m2.matrix.data)):
                for j in range(len(m2.matrix.data[i])):
                    temp[i][j] -= m2.matrix.data[i][j]
            s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp)
            return s

# 3. Multiply Matrix
# Operator Overloading for Multiplyinging Matrices

    def __mul__(self, m2):
        if (self.matrix.ncol != m2.matrix.nrow):  # checking Parameters
            raise incompaitableTypeException
        else:
            m3 = [[0 for x in range(m2.matrix.ncol)]
                  for y in range(self.matrix.nrow)]
            sum = 0
            for i in range(self.matrix.nrow):
                for j in range(m2.matrix.ncol):
                    for k in range(self.matrix.ncol):
                        sum += self.matrix.data[i][k]*m2.matrix.data[k][j]
                    m3[i][j] = sum
                sum = 0
        s = Matrix(nrow=self.matrix.nrow, ncol=m2.matrix.ncol, data=m3)
        return s

# 4. Divide Matrix
# A method just to avoid division by operator

    def __truediv__(self, m2):
        raise divisionErrorException("Can Matrices be divided ?")

# 5. Divide Matrix
# A method just to avoid floor division by operator
    def __floordiv__(self, m2):
        raise divisionErrorException

# Methods for Matrix Analysis

# 6.Equality
# A method which overrides operator for chechking equality of two matrices

    def __eq__(self, m2):
        if((self.matrix.dimensions == m2.matrix.dimensions)and(self.matrix.data == m2.matrix.data)):
            return True
        else:
            return False

# 7. isSquareMatrix
# a method to check if the matrix is square matrix or not

    def isSquareMatrix(self):
        if(self.matrix.nrow == self.matrix.ncol):
            return True
        else:
            return False

# 8. isInvertible
# a method to check if the matrix is invertible matrix or not

    def isInvertible(self):
        if(self.matrix.singular == True and self.matrix.invertibility == False):
            return False
        if(not self.isSquareMatrix()):
            return False
        else:
            self.determinantValue()
            if(self.matrix.determinant == 0):
                return False
            else:
                return True

# 9. copy
# returns a deep copy of the matrix object

    def copy(self):
        return copy.deepcopy(self)

# 10. getRow
# returns a specified row

    def getRow(self, index):
        temp = [[]]
        for j in range(self.matrix.ncol):
            temp[0].append(self.matrix.data[index][j])
        s = Matrix(nrow=1, ncol=self.matrix.ncol, data=temp)
        return s

# 11. getcol
# returns a specified column

    def getCol(self, index):
        temp = []
        for i in range(self.matrix.nrow):
            temp.append([])
            temp[i].append(self.matrix.data[i][index])
        s = Matrix(nrow=self.matrix.nrow, ncol=1, data=temp)
        return s

# 12. RoundOff
# rounds off all values to a certain degree

    def RoundOff(self, extent):
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                round(self.matrix.data[i][j], extent)

# 13. ScaleMatrix
# scales matrix values with a scalar

    def scaleMatrix(self, scalar):
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                self.matrix.data[i][j] *= scalar

# 14. DeterminantValue
# returns the determinant Value of the matrix

    def determinantValue(self):
        if(self.matrix.determinant == None):
            determinant = determinantHelper(self.matrix.data)
            self.matrix.determinant = determinant
            if(determinant == 0):
                self.matrix.invertibility = False
                self.matrix.singular = True
            return determinant
        else:
            pass
            return self.matrix.determinant

# 15. matrixRank
# returns the rank of the matrix

    def matrixRank(self):
        x = self.RrowEchleonTransform()
        rank = 0
        for i in range(x.matrix.nrow):
            for j in range(x.matrix.ncol):
                if(x.matrix.data[i][j] == 0):
                    pass
                if(x.matrix.data[i][j] == 1):
                    rank += 1
                    break
        self.matrix.rank = rank
        return rank

# Intermatrix Row and column operations

# 16. addRow
# adds row of matrix1 to row of matrix 2

    def addRow(self, index1, m2, index2):
        self.row_add(self.matrix.data[index1], m2.matrix.data[index2])

# 17. subRow
# subtracts row of matrix1 to row of matrix 2

    def subRow(self, index1, m2, index2):
        self.row_sub(self.matrix.data[index1], m2.matrix.data[index2])


# Transformations on matrices

    def invertMatrix(self):
        if(self.matrix.nrow != self.matrix.ncol):
            raise incompaitableTypeException
        if(self.matrix.invertibility == False):
            pass
        else:
            AM = self.matrix.data
            IM = identityMatrix(self.matrix.nrow, self.matrix.ncol).matrix.data
            for fd in range(len(AM)):
                if(AM[fd][fd] == 0):
                    AM[fd][fd] = 0.0000000000001
                fdScaler = 1.0 / AM[fd][fd]
                for j in range(len(AM)):
                    AM[fd][j] *= fdScaler
                    IM[fd][j] *= fdScaler
                for i in list(range(len(AM)))[0:fd] + list(range(len(AM)))[fd+1:]:
                    crScaler = AM[i][fd]
                    for j in range(len(AM)):
                        AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                        IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

            if(self.verify(IM)):
                self.matrix.singular = False
                for i in range(len(IM[i])):
                    for j in range(len(IM[i])):
                        IM[i][j] = round(IM[i][j], 2)
                self.matrix.data = IM
            else:
                self.matrix.determinant = 0
                self.matrix.singular = True
                raise nonInvertibleException

    def verify(self, m2):
        matrixs = []
        m1 = self.matrix.data
        im = []
        s = 0
        l = len(m1)
        for i in range(l):
            matrixs.append([])
            im.append([])
            for j in range(l):
                if(i == j):
                    im[i].append(1)
                else:
                    im[i].append(0)
                for k in range(l):
                    s += m1[i][k]*m2[k][j]
                matrixs[i].append(round(s, 1))
                s = 0

        if(matrixs == im):
            return True
        else:
            return False

    def row_add(self, row_left, row_right):
        return [a+b for (a, b) in zip(row_left, row_right)]

    def row_mult(self, row, num):
        return [x * num for x in row]

    def row_sub(self, row_left, row_right):
        return [a - b for (a, b) in zip(row_left, row_right)]

    def scalarDivideRow(self, row, value):
        return [(x/value) for x in row]

    def rowEchleonTransform(self):
        zx = self.copy()
        temp_mtx = zx.matrix.data

        def echelonify(rw, col):
            for i, row in enumerate(temp_mtx[(col+1):]):
                i += 1
                if rw[col] == 0:
                    continue
                temp_mtx[i+col] = self.row_sub(row,
                                               self.row_mult(rw, row[col] / rw[col]))
        for i in range(len(self.matrix.data)):
            active_row = temp_mtx[i]
            echelonify(active_row, i)
            temp_mtx = [[(0 if (0.0000000001 > x > -0.0000000001) else x)
                         for x in row] for row in temp_mtx]
        s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp_mtx)
        return s

    def RrowEchleonTransform(self):
        z = self.rowEchleonTransform().matrix.data
        for i in range(len(z)):
            if(z[i][i] != 1):
                z[i] = self.scalarDivideRow(z[i], z[i][i])
        if(self.matrix.nrow == self.matrix.ncol):
            IM = identityMatrix(self.matrix.ncol, self.matrix.nrow)
            while(z == IM.matrix.data):
                for j in range(len(z)):
                    for i in range(len(z[0])):
                        if(j == i):
                            continue
                        if(z[j][i] != 0):
                            self.row_sub(z[j], self.row_mult(z[i], z[i][j]))
        s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=z)
        return s

    def transposeTransform(self):
        c = []
        for i in range(self.matrix.ncol):
            c.append([])
            for j in range(self.matrix.nrow):
                c[i].append(self.matrix.data[j][i])
        s = Matrix(nrow=self.matrix.ncol, ncol=self.matrix.nrow, data=c)
        return s

# additional Methods

    def vectorMultiplication(self, v1):
        if(self.matrix.nrow != len(v1)):
            raise incompaitableTypeException
        else:
            vector = v1
            matrix = self.matrix.data
            c = []
            sum = 0
            for i in range(self.matrix.nrow):
                c.append([])
                for j in range(self.matrix.ncol):
                    sum += matrix[j][i]*vector[j]
                c[i].append(sum)
                sum = 0
            p = Matrix(ncol=1, nrow=len(v1), data=c)
            return p

    def strassenMultiplication(self, m1, m2):
        if(self.matrix.nrow != self.matrix.ncol and m2.matrix.nrow != m2.matrix.ncol):
            raise incompaitableTypeException
        else:
            if self.matrix.nrow == 2:
                return self.strassen2x2(m1, m2)
            else:
                if(self.matrix.nrow % 2 == 0):
                    m1 = self
                    n = self.matrix.nrow
                    self.strassenMultiplication(m1, m2)

    def eigenTerms(self):
        pass

    def strassen2x2(self, m1, m2):
        t1 = m1
        t2 = m2
        M1 = (t1[0][0]+t1[1][1])*(t2[0][0]+t2[1][1])
        M2 = (t1[1][0]+t1[1][1])*t2[0][0]
        M3 = t1[0][0]*(t2[0][1]-t2[1][1])
        M4 = t2[1][1]*(t2[1][0]-t2[0][0])
        M5 = (t1[0][0]+t1[0][1])*t2[1][1]
        M6 = (t1[1][0]-t1[0][0])*(t2[0][0]+t2[0][1])
        M7 = (t1[0][1]-t1[1][1])*(t2[1][0]+t2[1][1])
        mtx = [[M1+M4-M5+M7, M3+M5], [M2+M4, M1-M2+M3+M6]]
        return mtx

    def dotProduct(self, m2):
        sum = 0
        for row in range(self.matrix.nrow):
            for col in range(self.matrix.ncol):
                sum += self.matrix.data[row][col] * m2.matrix.data[row][col]
        return sum
    __repr__ = __str__

# Helper additional Methods
# zeroMatrix
# Creates a matrix with zeros of given shape and size


def zeroMatrix(nrow, ncol):
    t = []
    for i in range(nrow):
        t.append([])
        for j in range(ncol):
            t[i].append(0)
    s = Matrix(nrow=nrow, ncol=ncol, data=t)
    return s

# identityMatrix
# Creates a matrix with zeros of given shape and size


def identityMatrix(nrow, ncol):
    if(nrow == ncol):
        t = []
        for i in range(nrow):
            t.append([])
            for j in range(ncol):
                if(i == j):
                    t[i].append(1)
                else:
                    t[i].append(0)
        s = Matrix(nrow=nrow, ncol=ncol, data=t)
        return s
    else:
        raise incompaitableTypeException

# determinant helper
# helps with determinant calculations


def determinantHelper(x, sum=0):
    count = list(range(len(x)))
    if (len(x) == 2 and len(x[0]) == 2):
        v = x[0][0]*x[1][1] - x[0][1]*x[1][0]
        return v
    for i in count:
        cp = copy.deepcopy(x)
        cp = cp[1:]
        size = len(cp)
        for h in range(size):
            cp[h] = cp[h][0:i]+cp[h][i+1:]
        sign = pow((-1), (i % 2))
        subdet = determinantHelper(cp)
        sum += x[0][i]*sign*subdet
    return sum
