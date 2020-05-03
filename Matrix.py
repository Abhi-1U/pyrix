#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Name        : Pyrix/Matrix\n
Author      : Abhishek Ulayil\n
Contents    : 4 Exceptions Classes , 2 Function classes , 43 methods\n
Description : A simple matrix manipulation library  \n
Encoding    : UTF-8\n
Version     : 0.8.82
--------------------------------------------------------------------
"""
import random
import copy


class ExceptionTemplate(Exception):
    def __call__(self, *args):
        return self.__class__(*(self.args + args))

    def __str__(self):
        return ': '.join(self.args)


class bitWiseOnMatrix(ExceptionTemplate):
    """Traditional Bitwise Operators are not allowed to work on matrix objects as of now. Maybe in future we will find a creative use case of them.
    """


class binaryMatrixException(ExceptionTemplate):
    """Not a Binary Matrix
    """


class divisionErrorException(ExceptionTemplate):
    """Can Matrices be Divided ?"""


class incompaitableTypeException(Exception):
    """If you come across this Exception then the issue is probably out of these four cases:\n
        Case 1: The dimensions of matrices dont match for the operation to happen\n
        Case 2: The matrix is not a square matrix\n
        Case 3: The matrices do not satisfy the condition for multiplication\n
        Case 4: The Data of the Matrix is not of the Dimensions Given.
    """


class nonInvertibleException(Exception):
    """Matrix is not invertible due to its singular nature and determinant being zero"""


class matrixData(object):
    """ All The Matrix Data is stored here which allows for implementing Dynamic Programming Principles such as Memoization:\n
        Data List:
        1.nrow[int]: Number of Rows
        2.ncol[int]: Number of Columns
        3.dimensions[list]: list format of nrow,ncol together
        4.data[list]: All the Matrix Values stored in nested-list format
        5.invertibility[Boolean]: returns True if matrix is invertible ,default-value=None
        6.determinant[int]: stores determinant value,default-value=None
        7.singular[Boolean]: returns False if matrix is invertible ,default-value=None
        8.eigenvals[list]: list of eigen values
        9.eigenvects[list]: list of eigen vectors
        10.rank[int]: stores the rank of the matrix
        11.triangularity[int]: returns 2 for upperT. ,1 for lowerT.,0 for No Triangularity
    """

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
        self.triangularity = None
        self.binaryMatrix = False

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
Function List:
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
20. Random Matrix
"""


class Matrix:
    """ Get Started By Creating a Matrix Object\n
        ncol=number of cols\n
        nrow=number of rows\n
        data=corresponding matrix data of the dimensions as a list\n
        eg. mat = M.Matrix(nrow=2,ncol=2,data=[[1,1],[1,1]])\n
    """

    def __init__(self, nrow=1, ncol=1, data=[1]):
        if(len(data) == nrow, len(data[0]) == ncol):
            self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)
        else:
            raise incompaitableTypeException

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
            s = Matrix(nrow=self.matrix.nrow,
                       ncol=self.matrix.ncol, data=temp)
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
            s = Matrix(nrow=self.matrix.nrow,
                       ncol=self.matrix.ncol, data=temp)
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

    def __pow__(self, times):
        for i in range(times):
            self *= self
        return self

    def __abs__(self):
        pass
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
        """ Checks if the Matrix is a square Matrix or not\n
             A square matrix is a matrix with equal number of rows and cols\n
             returns a Boolean value
        """
        if(self.matrix.nrow == self.matrix.ncol):
            return True
        else:
            return False

# 8. isInvertible
# a method to check if the matrix is invertible matrix or not

    def isInvertible(self):
        """ Checks if the Matrix is an Invertible Matrix or not\n
             An Invertible matrix is a matrix with a non zero determinant \n
             returns a Boolean value
        """
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

    def isBinaryMatrix(self):
        pass
# 9. copy
# returns a deep copy of the matrix object

    def copy(self):
        """ Creates a DEEP(HARD) copy of the Matrix object\n
            Returns a Matrix Object
        """
        return copy.deepcopy(self)

# 10. getRow
# returns a specified row

    def getRow(self, index):
        """Selects a Row of the matrix of specified index\n
            Returns a list of the values
        """
        temp = [[]]
        for j in range(self.matrix.ncol):
            temp[0].append(self.matrix.data[index][j])
        s = Matrix(nrow=1, ncol=self.matrix.ncol, data=temp)
        return s

# 11. getcol
# returns a specified column

    def getCol(self, index):
        """Selects a Column of the matrix of specified index\n
            Returns a list(or nested list) of the values
        """
        temp = []
        for i in range(self.matrix.nrow):
            temp.append([])
            temp[i].append(self.matrix.data[i][index])
        s = Matrix(nrow=self.matrix.nrow, ncol=1, data=temp)
        return s

# 12. RoundOff
# rounds off all values to a certain degree

    def RoundOff(self, extent):
        """Rounds off the Value of the data in the matrix object to the given extent\n
            Returns NoneType and should not be assigned to a variable
        """
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                self.matrix.data[i][j] = round(self.matrix.data[i][j], extent)

# 13. ScaleMatrix
# scales matrix values with a scalar

    def scaleMatrix(self, scalar):
        """Scales the Value of the data in the matrix object by the scalar value\n
            Returns NoneType and should not be assigned to a variable
        """
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                self.matrix.data[i][j] *= scalar

# 14. DeterminantValue
# returns the determinant Value of the matrix

    def determinantValue(self):
        """Determines the determinant value of the matrix object \n
            Returns int or float depending on the outcome
        """
        if(self.matrix.determinant == None):
            determinant = self.__determinantHelper(self.matrix.data)
            self.matrix.determinant = determinant
            if(determinant == 0):
                self.matrix.invertibility = False
                self.matrix.singular = True
            return determinant
        else:
            pass
            return self.matrix.determinant
# 15. determinant helper
# helps with determinant calculations

    def __determinantHelper(self, x, sum=0):
        count = list(range(len(x)))
        if (len(x) == 2 and len(x[0]) == 2):
            v = x[0][0]*x[1][1] - x[0][1]*x[1][0]
            return v
        for i in count:
            cp = copy.deepcopy(x)
            cp = cp[1:]
            size = len(cp)
            for h in range(size):
                cp[h] = cp[h][0: i]+cp[h][i+1:]
            sign = pow((-1), (i % 2))
            subdet = self.__determinantHelper(cp)
            sum += x[0][i]*sign*subdet
        return sum

# 16. matrixRank
# returns the rank of the matrix

    def matrixRank(self):
        """Calculates the Rank of the matrix object \n
            Returns integer value of rank
        """
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

    def isUpperTriangularMaatrix(self):
        pass

    def isLowerTriangularMatrix(self):
        pass

# Intermatrix Row and column operations

# 17. addRow
# adds row of matrix1 to row of matrix 2

    def addRows(self, index1, m2, index2):
        """Adds row values of one matrix to another matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.__row_add(self.matrix.data[index1], m2.matrix.data[index2])

# 18. subRow
# subtracts row of matrix1 to row of matrix 2

    def subRows(self, index1, m2, index2):
        """Subtracts row values of one matrix to another matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.__row_sub(self.matrix.data[index1], m2.matrix.data[index2])

# IntraMatrix Row and Col Operations
# Coming soon!
    def addRow(self, index1, index2):
        """Adds row values of one matrix to same matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.__row_add(self.matrix.data[index1], self.matrix.data[index2])

    def subRow(self, index1, index2):
        """Subtracts row values of one matrix to same matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.__row_sub(self.matrix.data[index1], self.matrix.data[index2])
# Transformations on matrices

# 19. Invert Matrix
# returns a new object of inverted matrix

    def invertMatrix(self):
        """Creates an Inverse Matrix of the given matrix\n
            Returns a Matrix object 
        """
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
                for i in list(range(len(AM)))[0: fd] + list(range(len(AM)))[fd+1:]:
                    crScaler = AM[i][fd]
                    for j in range(len(AM)):
                        AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                        IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

            if(self.__verify(IM)):
                self.matrix.singular = False
                for i in range(len(IM[i])):
                    for j in range(len(IM[i])):
                        IM[i][j] = round(IM[i][j], 2)
                self.matrix.data = IM
            else:
                self.matrix.determinant = 0
                self.matrix.singular = True
                raise nonInvertibleException

# 20.Helper Method for inversion
# Verifies the matrix for proper inversion
    def __verify(self, m2):
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

# 21. micro method for adding rows

    def __row_add(self, row_left, row_right):
        return [a+b for (a, b) in zip(row_left, row_right)]

# 22. micro method for scaling rows

    def __row_mult(self, row, num):
        return [x * num for x in row]

# 23. micro method for subtracting rows

    def __row_sub(self, row_left, row_right):
        return [a - b for (a, b) in zip(row_left, row_right)]

# 24. micro method for dividng row with scalar

    def __scalarDivideRow(self, row, value):
        return [(x/value) for x in row]

# 25.RowEchleonTransform
# returns the rowechleon form of the matrix

    def rowEchleonTransform(self):
        zx = self.copy()
        temp_mtx = zx.matrix.data

        def echleonS(rw, col):
            for i, row in enumerate(temp_mtx[(col+1):]):
                i += 1
                if rw[col] == 0:
                    continue
                temp_mtx[i+col] = self.__row_sub(row,
                                                 self.__row_mult(rw, row[col] / rw[col]))
        for i in range(len(self.matrix.data)):
            active_row = temp_mtx[i]
            echleonS(active_row, i)
            temp_mtx = [[(0 if (0.0000000001 > x > -0.0000000001) else x)
                         for x in row] for row in temp_mtx]
        s = Matrix(nrow=self.matrix.nrow,
                   ncol=self.matrix.ncol, data=temp_mtx)
        return s

# 26.RRowEchleonTransform
# returns the reduced rowechleon form of the matrix

    def RrowEchleonTransform(self):
        z = self.rowEchleonTransform().matrix.data
        for i in range(len(z)):
            if(z[i][i] != 1):
                z[i] = self.__scalarDivideRow(z[i], z[i][i])
        if(self.matrix.nrow == self.matrix.ncol):
            IM = identityMatrix(self.matrix.ncol, self.matrix.nrow)
            while(z == IM.matrix.data):
                for j in range(len(z)):
                    for i in range(len(z[0])):
                        if(j == i):
                            continue
                        if(z[j][i] != 0):
                            self.__row_sub(
                                z[j], self.__row_mult(z[i], z[i][j]))
        s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=z)
        return s

# 27.transposeTransform
# returns the transpose of the matrix

    def transposeTransform(self):
        c = []
        for i in range(self.matrix.ncol):
            c.append([])
            for j in range(self.matrix.nrow):
                c[i].append(self.matrix.data[j][i])
        s = Matrix(nrow=self.matrix.ncol, ncol=self.matrix.nrow, data=c)
        return s

# additional Methods

# 28.vectorMultiplication
# multiplication of vector as a matrix with another matrix

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

# 29.StrassenMultiplication
# returns multiplication of two matrices with strassen method

    def strassenMultiplication(self, m1, m2):
        if(self.matrix.nrow != self.matrix.ncol and m2.matrix.nrow != m2.matrix.ncol):
            raise incompaitableTypeException
        else:
            if self.matrix.nrow == 2:
                return self.__strassen2x2(m1, m2)
            else:
                if(self.matrix.nrow % 2 == 0):
                    m1 = self
                    n = self.matrix.nrow
                    self.strassenMultiplication(m1, m2)

# 30.eigenTerms
# returns the eigenValues and eigenVects of the matrix

    def eigenTerms(self):
        pass

# 31.strassen2x2
# helper method for 2x2matrix multiplications by strassen method

    def __strassen2x2(self, m1, m2):
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

# 32.dotproduct
# for vectors as matrix

    def dotProduct(self, m2):
        sum = 0
        for row in range(self.matrix.nrow):
            for col in range(self.matrix.ncol):
                sum += self.matrix.data[row][col] * m2.matrix.data[row][col]
        return sum
# Matrix Equation Methods

    def adjointTransform(self):
        pass

    def minorSpecific(self, row, column):
        pass

    def cofactor(self):
        pass

    def getAllMinors(self):
        pass

    def getCofactorMatrix(self):
        pass

    def ALUTransform(self):
        pass

    def augmentedMatrix(self):
        pass

    def LUdecomposition(self):
        pass

    def JordanGuassElimination(self):
        pass

    __repr__ = __str__


# Quick Initialization  Methods

# zeroMatrix
# Creates a matrix with zeros of given shape and size


def zeroMatrix(nrow, ncol):
    """Create a zero matrix of the given dimensions\n
        Retuns a Matrix Object 
    """
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
    """Create a identity matrix of the given dimensions\n
        Works for square Matrices\n
        Retuns a Matrix Object 
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
        s = Matrix(nrow=nrow, ncol=ncol, data=t)
        return s
    else:
        raise incompaitableTypeException

# random Matrix
# generates a randomized matrix depending on the scale and type


def randomMatrix(scale, type):
    if(scale == "small" and type == "int"):
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for j in range(ncol):
                data[i].append(random.randint(1, 100))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if(scale == "large" and type == "int"):
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for j in range(ncol):
                data[i].append(random.randint(10, 10000))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s

    if(scale == "small" and type == "float"):
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for j in range(ncol):
                data[i].append(random.triangular(low=0.0, high=10.0))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if(scale == "large" and type == "float"):
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for j in range(ncol):
                data[i].append(random.triangular(low=0.0, high=1000.0))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
