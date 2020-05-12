#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Name        : Pyrix/Matrix\n
Author      : Abhishek Ulayil\n
Contents    : 4 Exceptions Classes , 2 Function classes , 43 methods\n
Description : A simple matrix manipulation library  \n
Encoding    : UTF-8\n
Version     : 0.4.10    
--------------------------------------------------------------------
"""
import random
import copy
import math
import json
import csv
from filepath import fileChooserUI, folderChooserUI


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
        12.binaryMatrix[Boolean]: returns True if binary matrix//reserved for binary matrix class
        13.singularvalue[int/float]:returns singular value,None By default
        14.orthogonalMatrix[Boolean]:returns True if matrix is orthogonal in nature
        15.minor[list]: contains minor values,By default None 
        16.listifieddata[list]: contains all the data values in a flattened list
    """

    def __init__(self, nrow, ncol, data):
        self.classType = 'Matrix'
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
        self.trace = None
        self.triangularity = None
        self.binaryMatrix = False
        self.singularvalue = None
        self.orthogonalMatrix = False
        self.minor = None
        self.listifieddata = []

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
21. Unit Matrix
22. matrixTrace
23. adjoint
24. cofactor
25. minor
26. isUpperTriangular
27. isLowerTriangular
28. listifymatrix
29. switchAxis
30. reDimensionalize
31. JSONEncoder
32. JSONDecoder
33. JSONExport
34. JSONImport
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
        if(self.isSquareMatrix()):
            for i in range(times):
                self *= self
            return self
        else:
            raise incompaitableTypeException

    def __abs__(self):
        if(self.matrix.determinant == None):
            return self.determinantValue()
        else:
            return self.matrix.determinant
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

    def __trunc__(self):
        truncMatrix = []
        for i in range(self.matrix.nrow):
            truncMatrix.append([])
            for j in range(self.matrix.ncol):
                truncMatrix[i].append(math.trunc(self.matrix.data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=truncMatrix)

    def __ceil__(self):
        ceilMatrix = []
        for i in range(self.matrix.nrow):
            ceilMatrix.append([])
            for j in range(self.matrix.ncol):
                ceilMatrix[i].append(math.ceil(self.matrix.data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=ceilMatrix)

    def __floor__(self):
        floorMatrix = []
        for i in range(self.matrix.nrow):
            floorMatrix.append([])
            for j in range(self.matrix.ncol):
                floorMatrix[i].append(math.floor(self.matrix.data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=floorMatrix)
# Methods for Matrix Analysis

# 6.Equality
# A method which overrides operator for chechking equality of two matrices

    def __eq__(self, matrix2):
        return self.equals(matrix2)

    def equals(self, matrix2):
        """Checks for equality of the two matrices\n
            based on dimensions and the data inside.
            Returns a Boolean Value
        """
        if((self.matrix.dimensions == matrix2.matrix.dimensions)and(self.matrix.data == matrix2.matrix.data)):
            return True
        else:
            return False
# 7. isSquareMatrix
# a method to check if the matrix is square matrix or not

    def isSquareMatrix(self):
        """ Checks if the Matrix is a square Matrix or not\n
             A square matrix is a matrix with equal number of rows and cols\n
             Returns a Boolean value
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
             Returns a Boolean value
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
            if(self.isSquareMatrix()):
                determinant = self.__determinantHelper(self.matrix.data)
                self.matrix.determinant = determinant
                if(determinant == 0):
                    self.matrix.invertibility = False
                    self.matrix.singular = True
                return determinant
            else:
                raise incompaitableTypeException
        else:
            pass
            return self.matrix.determinant
# 15. determinant helper
# helps with determinant calculations

    def __determinantHelper(self, x, sum=0):
        """This Method specifically helps with recursive implementation of determinant algorithm.
        """
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

    def matrixTrace(self):
        trace = 0
        if(self.isSquareMatrix()):
            for i in range(self.matrix.nrow):
                trace += self.matrix.data[i][i]
        self.matrix.trace = trace
        return trace

    def isUpperTriangularMatrix(self):
        isUpperTriangularMatrix = True
        isLowerTriangularMatrix = True
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                if(i < j)and (self.matrix.data[i][j] != 0):
                    isUpperTriangularMatrix = False
                if(i > j)and (self.matrix.data[i][j] != 0):
                    isLowerTriangularMatrix = False
        if(isUpperTriangularMatrix) and (not isLowerTriangularMatrix):
            self.matrix.triangularity = 2
            return True
        else:
            return False

    def isLowerTriangularMatrix(self):
        isUpperTriangularMatrix = True
        isLowerTriangularMatrix = True
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                if(i < j)and (self.matrix.data[i][j] != 0):
                    isUpperTriangularMatrix = False
                if(i > j)and (self.matrix.data[i][j] != 0):
                    isLowerTriangularMatrix = False
        if(isLowerTriangularMatrix)and (not isUpperTriangularMatrix):
            self.matrix.triangularity = 1
            return True
        else:
            return False

# Intermatrix Row and column operations

# 17. addRow
# adds row of matrix1 to row of matrix 2

    def addRows(self, index1, m2, index2):
        """Adds row values of one matrix to another matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.matrix.data[index1] = self.__row_add(
            self.matrix.data[index1], m2.matrix.data[index2])

# 18. subRow
# subtracts row of matrix1 to row of matrix 2

    def subRows(self, index1, m2, index2):
        """Subtracts row values of one matrix to another matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.matrix.data[index1] = self.__row_sub(
            self.matrix.data[index1], m2.matrix.data[index2])

# IntraMatrix Row and Col Operations
# Coming soon!
    def addRow(self, index1, index2):
        """Adds row values of one matrix to same matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.matrix.data[index1] = self.__row_add(
            self.matrix.data[index1], self.matrix.data[index2])

    def subRow(self, index1, index2):
        """Subtracts row values of one matrix to same matrix\n
            Returns NoneType and should not be assigned to a variable
        """
        self.matrix.data[index1] = self.__row_sub(
            self.matrix.data[index1], self.matrix.data[index2])
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
        """This method verifies a unverse of the matrix by multiplying it with the orignal input matrix to get identity matrix.
        """
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
        temp = zx.matrix.data

        def echleonS(rw, col):
            for i, row in enumerate(temp[(col+1):]):
                i += 1
                if rw[col] == 0:
                    continue
                temp[i+col] = self.__row_sub(row,
                                             self.__row_mult(rw, row[col] / rw[col]))
        for i in range(len(self.matrix.data)):
            current_row = temp[i]
            echleonS(current_row, i)
            temp = [[(0 if (0.0000000001 > x > -0.0000000001) else x)
                     for x in row] for row in temp]
        s = Matrix(nrow=self.matrix.nrow,
                   ncol=self.matrix.ncol, data=temp)
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

    def strassenMultiplication(self, m1, m2, nrows, ncols):

        if(nrows[0] != ncols[0] and nrow[1] != ncols[1]):
            raise incompaitableTypeException
        else:
            if nrows[0] == 2:
                return self.__strassen2x2(m1, m2)
            else:
                if(nrows[0] % 2 == 0):
                    p1 = self.__partitionmatrix(
                        m1, nrow=nrows[0], ncol=ncols[0])
                    p1 = self.__partitionmatrix(
                        m2, nrow=nrows[1], ncol=ncols[1])
                    newval = nrows[0]/4
                    returnmatrix=[]
                    for minimatrix1,minimatrix2 in zip(p1,p2):
                        returnmatrix.append(self.strassenMultiplication(minimatrix1,minimatrix2,nrows=[newval,newval],ncols=[newval,newval]))
                    self.__combinedata(returnmatrix)
                    return returnmatrix
    def __partitionmatrix(self, data, nrow, ncol):
        parts = 4
        newnrow = nrow/parts
        newncol = ncol/parts
        quadrant1 = []
        quadrant2 = []
        quadrant3 = []
        quadrant4 = []
        quadrant2.append(data[0:newnrow][0:newncol])
        quadrant1.append(data[newnrow:][0:newncol])
        quadrant3.append(data[0:newnrow][newncol:])
        quadrant4.append(data[newnrow:][newncol:])
        return [quadrant2, quadrant1, quadrant3, quadrant4]

    def __combinedata(self, matrix1, matrix2, matrix3, matrix4):
        return
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
        cofactor = self.getAllCofactors()
        return cofactor.transposeTransform()

    def minorSpecific(self, row, column):
        if self.matrix.minor == None:
            self.getAllMinors()
        else:
            pass
        return self.matrix.minor[row][column]

    def cofactorSpecific(self, row, column):
        return self.getAllCofactors().matrix.data[row][column]

    def getAllMinors(self):
        matrixdata = self.matrix.data
        if(self.isSquareMatrix()):
            if (self.matrix.dimensions == [2, 2]):
                allminorslist = self.__minor2x2(matrixdata)
            else:
                allminorslist = self.__minor(matrixdata)
            self.matrix.minor = allminorslist
            return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=self.matrix.minor)
        else:
            raise incompaitableTypeException

    def getAllCofactors(self):
        if(self.matrix.minor == None):
            self.getAllMinors()
        else:
            pass
        cofactors = self.__cofactor(self.matrix.minor)
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=cofactors)

    def ALUTransform(self):
        pass

    def augmentedMatrix(self):
        pass

    def LUdecomposition(self):
        pass

    def JordanGuassElimination(self):
        pass

    def __minor2x2(self, matrixdata):
        return [[matrixdata[1][1], matrixdata[1][0]], [matrixdata[0][1], matrixdata[0][0]]]

    def __cofactor(self, minorlist):
        cofactors = []
        for i in range(self.matrix.nrow):
            cofactors.append([])
            for j in range(self.matrix.ncol):
                cofactors[i].append(minorlist[i][j]*pow(-1, i+j+2))
        return cofactors

    def __minor(self, matrixdata):
        minors = []
        for i in range(len(matrixdata)):
            minors.append([])
            for j in range(len(matrixdata[0])):
                minors[i].append(self.__determinantHelper(
                    self.__matrixsplitter(matrixdata, i, j)))
        return minors

    def __matrixsplitter(self, matrixdata, exceptionrow, exceptioncol):
        excludedmatrix = []
        returnmatrix = []
        iterator = 0
        for i in range(len(matrixdata)):
            for j in range(len(matrixdata[i])):
                if([i, j] == [exceptionrow, j]):
                    continue
                if([i, j] == [i, exceptioncol]):
                    continue
                else:
                    excludedmatrix.append(matrixdata[i][j])
                    iterator += 1
        dimensions = math.sqrt(len(excludedmatrix))
        for i in range(int(dimensions)):
            returnmatrix.append([])
            returnmatrix[i] = excludedmatrix[0:int(dimensions)]
            del excludedmatrix[0: int(dimensions)]
        return returnmatrix

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

# unit Matrix
# Creates a Matrix with ones of given size and shape


def unitMatrix(nrow, ncol):
    """Create a unit matrix of the given dimensions\n
        Retuns a Matrix Object 
    """
    t = []
    for i in range(nrow):
        t.append([])
        for j in range(ncol):
            t[i].append(1)
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


def listifyMatrix(MatrixObject):
    matrixdata = MatrixObject.matrix.data
    listifiedmatrix = []
    for i in range(MatrixObject.matrix.nrow):
        for j in range(MatrixObject.matrix.ncol):
            listifiedmatrix.append(matrixdata[i][j])
    MatrixObject.matrix.listifieddata = listifiedmatrix
    return listifiedmatrix


def nestifyMatrix(listeddata, rowcount, colcount):
    clist = listeddata
    nested = []
    for i in range(rowcount):
        nested.append(clist[i:colcount])
        del clist[i:colcount]
    return nested


def reDimensionalize(MatrixObject, nrow, ncol):
    listifieddata = listifyMatrix(MatrixObject)
    matrixdata = []
    for i in range(nrow):
        matrixdata.append([])
        matrixdata[i] = listifieddata[0:ncol]
        del listifieddata[0:ncol]
    return Matrix(nrow=nrow, ncol=ncol, data=matrixdata)


def switchAxis(MatrixObject):
    newcol = MatrixObject.matrix.nrow
    newrow = MatrixObject.matrix.ncol
    return reDimensionalize(MatrixObject, newrow, newcol)


def InterpretMatrix(nrow, ncol, data):
    if(type(data) == str):
        pass
    if(type(data) == list):
        if(type(data[0]) == list):
            pass
        if(type(data[0]) == str):
            pass
        if(type(data[0]) == tuple):
            pass
        if(type(data[0]) == Matrix):
            pass
        if(type(data[0]) == set):
            pass
        if(type(data[0]) == int) or (type(data[0]) == float):
            pass


def JSONEncoder(object):
    """Encodes dictionary data of the Matrix Object into JSON format.
    """
    Object = object
    return Object.matrix.__dict__


def JSONExport(Object, filename):
    """Exports the Object data as an JSON file to save th eobject permanantely.
    """
    data = JSONEncoder(Object)
    with open(filename, "w") as outfile:
        json.dump(data, outfile)
    print("Export Of Object Data Successfull!")


def JSONDecoder(object):
    """Decodes JSON File type\n 
        returns a Matrix Object.
    """
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
    if classtype == 'Matrix':
        returnMatrix = Matrix(nrow=nrow, ncol=ncol, data=data)
        for key, item in object.items():
            setattr(returnMatrix.matrix, key, item)
    print("JSON Import Successfull !")
    return returnMatrix


def JSONImport(filename, mode="UI"):
    """Allows for JSON files to be read and recreate the objects\n
        If you have Tkinter installed then the UI mode will trigger the GUI to select file.
        Returns a Matrix Object.
    """
    if(mode == "UI"):
        filepath = fileChooserUI()
    else:
        filepath = filename
    with open(filepath, 'r') as openfile:
        json_object = json.load(openfile)
        openfile.close()
    return JSONDecoder(json_object)


def CSVImport(filename, mode="UI"):
    if(mode == "UI"):
        filepath = fileChooserUI()
    else:
        filepath = filename
    with open(filepath, 'r') as openfile:
        csvfile = csv.reader(openfile, delimiter=',')
        dataoutput = CSVDecoder(csvfile)
        openfile.close()
    return dataoutput


def CSVDecoder(csvobject):
    reader = csvobject
    data = []
    for row in reader:
        for items in row:
            data.append()
    return data
