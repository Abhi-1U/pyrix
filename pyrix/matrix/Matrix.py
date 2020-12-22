#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/Matrix
Author      : Abhi-1U <https://github.com/Abhi-1U>
Description : A simple matrix manipulation library
Encoding    : UTF-8
Version     :0.7.19
Build       :0.7.19/21-12-2020
"""
# *------- Imports ------------------------------------------------------------*
import copy
import math
from pyrix.exception import (
    bitWiseOnMatrix,
    divisionErrorException,
    incompaitableTypeException,
    nonInvertibleException,
)
import random
# *----------------------------------------------------------------------------*

# *------- matrixData ---------------------------------------------------------*
# * This is the primary data object in pyrix/Matrix and pyrix/BinaryMatrix.
# * MatrixData includes a ton of meta-Data which allows for enhanced Features,
# * Performance and Computational Savings.
# * A Dynamic Memoization Technique is also integrated in performance critical
# * areas of the library ,however there are at times where the data memoized
# * becomes outdated and hence needs to be recalculated to maintain Integrity
# * and accuracy of calculations.
# *
# * Pyrix(Python Implementation) Balances these two aspects and has been
# * implemented from scratch in python V3 only .
# * With a vision of Python based web Applications in mind dataTypes used
# * are JSON friendly.
# * A list of MetaData Stored and descriptions are bundled along with the
# * docstrings included with the class .
# * ---------------------------------------------------------------------------*
class matrixData(object):
    """
    All The Matrix Data is stored here which allows for implementing Dynamic
    Programming Principles such as Memoization:
    Data List:
        1.nrow[int]: Number of Rows.
        2.ncol[int]: Number of Columns.
        3.dimensions[list]: list format of nrow,ncol together.
        4.data[list]: All the Matrix Values stored in nested-list format.
        5.invertibility[Boolean]: returns True if matrix is invertible ,
            default-value=None.
        6.determinant[int]: stores determinant value,default-value=None.
        7.singular[Boolean]: returns False if matrix is invertible ,
            default-value=None.
        8.eigenvals[list]: list of eigen values.
        9.eigenvects[list]: list of eigen vectors.
        10.rank[int]: stores the rank of the matrix.
        11.triangularity[int]: returns 2 for upperT. ,1 for lowerT.,0 for No
            Triangularity.
        12.binaryMatrix[Boolean]: returns True if binary matrix//reserved
            for binary matrix class.
        13.singularvalue[int/float]:returns singular value,None By default.
        14.orthogonalMatrix[Boolean]:returns True if matrix is orthogonal in
            nature.
        15.minor[list]: contains minor values,By default None.
        16.listifieddata[list]:contains all the data values in a flattened list.
        17.classtype[str]: defines the type of pyrix/matrix implementation
            (occours in inheriting classes).
        18.symmetry[Boolean]:True for symmetrical,None by default,False
            otherwise.
        19.mode[str]: Represents mode of operation for some value
    """

    def __init__(self, nrow, ncol, data):
        self.classType = "Matrix"
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
        self.symmetry = None
        self.mode = None
        self.identityMatrix=None

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(name)

    def __delattr__(self, name):
        del self.__dict__[name]


# *------- Matrix -------------------------------------------------------------*
# * pyrix/Matrix is the core Module and intuitively places an implementation
# * of Abstract/Computer Representation of Matrix in general .
# * The primary reason for such Development was to simplify dependence on C
# * based libraries used in backend of many popular python packages.
# * C based libraries are tried and tested and these python packages refine
# * the user experience quite a lot but, as an enthusiast i imagine if python
# * was like some other restrictive language which did not allow C API ,there
# * would surely had been some library built from scratch in python.
# *
# * We live in a world of Developers / Coders who rightfully use existing
# * libraries and do it in a beautiful way of their own,thinking why reinvent
# * the wheel when there are bigger problems to tackle. I agree with them
# * But as a low level developer i find myself at peace creating my own libs
# * and utilize them to the fullest in an efficient manner. :)
# *
# * Functions/Methods Covered
# * 1. Initialization Matrix
# * 2. Add/Subtract/Multiply
# * 3. Equality Check
# * 4. Inversion
# * 5. Add_row, Sub_row, Multiply_row, getrow, getcol
# * 6. RowEchleonTransform
# * 7. Copy
# * 8. Transpose
# * 9. determinant
# * 10. Vector Multiplication
# * 11. scale
# * 12. Strassen Multiplication
# * 13. Identity Matrix
# * 14. zero Matrix
# * 15. isSquareMatrix
# * 16. isInvertible
# * 17. RoundOff
# * 18. Rank
# * 19. ReducedRowEchleonTransform
# * 20. Random Matrix
# * 21. Unit Matrix
# * 22. matrixTrace
# * 23. adjoint
# * 24. cofactor
# * 25. minor
# * 26. isUpperTriangular
# * 27. isLowerTriangular
# * 28. listifymatrix
# * 29. flipDimesnsions
# * 30. reDimensionalize
# * 31. JSONEncoder
# * 32. JSONDecoder
# * 33. JSONExport
# * 34. JSONImport
# * 35. isSymmetricMatrix
# * 36. isOrthogonalMatrix
# * 37. globalMean/LocalRowMean/LocalColumnMean
# * 38. globalMedian/LocalRowMedian/LocalColumnMedian
# * 39. globalMode/LocalRowMode/LocalColumnMode
# *----------------------------------------------------------------------------*


class Matrix:
    """ Get Started By Creating a Matrix Object\n
        ncol=number of cols\n
        nrow=number of rows\n
        data=corresponding matrix data of the dimensions as a list\n
        eg. mat = M.Matrix(nrow=2,ncol=2,data=[[1,1],[1,1]])\n
    """

    def __init__(self, nrow=1, ncol=1, data=[[1]]):
        if (len(data) == nrow) and (len(data[0]) == ncol):
            self.matrix = matrixData(nrow=nrow, ncol=ncol, data=data)
        else:
            raise incompaitableTypeException

    def __repr__(self):
        pass

    def __str__(self):
        stringV = str()
        stringV = "Matrix:\n"
        for item in self.matrix.data:
            stringV += str(item) + "\n"
        stringV += (
            "Dimensions :"
            + str(self.matrix.dimensions[0])
            + "x"
            + str(self.matrix.dimensions[1])
        )
        return stringV
    
    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(name)

    def __delattr__(self, name):
        del self.__dict__[name]
    
    def __getitem__(self,key):
        if(isinstance(key, int)):
            return self.matrix.data[key]
        if(isinstance(key,(list,tuple)) and len(key)==2):
            return self.matrix.data[key[0]][key[1]]
        else:
            print("MultiDimensional Matrix in Works")
    
    def __setitem__(self,key,value):
        if(isinstance(key, int)):
            self.matrix.data[key]=value
        if(isinstance(key,(list,tuple)) and len(key)==2):
            self.matrix.data[key[0]][key[1]]=value
        else:
            print("MultiDimensional Matrix in Works")
    # *------- Basic Operations on Matrices -----------------------------------*

    # *------- Add Matrix -----------------------------------------------------*

    def __add__(self, m2):
        if self.matrix.dimensions != m2.matrix.dimensions:
            raise incompaitableTypeException
        else:
            temp = Copy(self.matrix.data)
            for i in range(len(m2.matrix.data)):
                for j in range(len(m2.matrix.data[i])):
                    temp[i][j] += m2.matrix.data[i][j]
            s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp)
            return s

    # *------- Subtract Matrix ------------------------------------------------*
    
    def __sub__(self, m2):
        if self.matrix.dimensions != m2.matrix.dimensions:
            raise incompaitableTypeException
        else:
            temp = Copy(self.matrix.data)
            for i in range(len(m2.matrix.data)):
                for j in range(len(m2.matrix.data[i])):
                    temp[i][j] -= m2.matrix.data[i][j]
            s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp)
            return s

    # *------- Multiply Matrix ------------------------------------------------*
    
    def __mul__(self, m2):
        if self.matrix.ncol != m2.matrix.nrow:  # checking Parameters
            raise incompaitableTypeException
        else:
            m3 = [[0 for x in range(m2.matrix.ncol)] for y in range(self.matrix.nrow)]
            sum = 0
            for i in range(self.matrix.nrow):
                for j in range(m2.matrix.ncol):
                    for k in range(self.matrix.ncol):
                        sum += self.matrix.data[i][k] * m2.matrix.data[k][j]
                    m3[i][j] = sum
                    sum = 0
        s = Matrix(nrow=self.matrix.nrow, ncol=m2.matrix.ncol, data=m3)
        return s

    # *------- Power ----------------------------------------------------------*

    def __pow__(self, times):
        assert isinstance(times, int), "Float not allowed"
        if self.isSquareMatrix():
            for _i in range(times-1):
                self = self*self
            return self
        else:
            raise incompaitableTypeException
    # *------- Absolute -------------------------------------------------------*
    def __abs__(self):
        if self.matrix.determinant == None:
            return self.determinantValue()
        else:
            return self.matrix.determinant

    # *------- Divide Matrix --------------------------------------------------*

    def __truediv__(self, m2):
        raise divisionErrorException("Can Matrices be divided ?")

    # *------- Floor Divide Matrix --------------------------------------------*

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
    
    # *------- Truncate(R->I 0) -----------------------------------------------*

    def __trunc__(self):
        truncMatrix = []
        for i in range(self.matrix.nrow):
            truncMatrix.append([])
            for j in range(self.matrix.ncol):
                truncMatrix[i].append(math.trunc(self.matrix.data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=truncMatrix)

    # *------- Ceilate(R->I FOR >=X) -----------------------------------------*

    def __ceil__(self):
        ceilMatrix = []
        for i in range(self.matrix.nrow):
            ceilMatrix.append([])
            for j in range(self.matrix.ncol):
                ceilMatrix[i].append(math.ceil(self.matrix.data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=ceilMatrix)

    # *------- Floor(R->I FOR <=X) -------------------------------------------*

    def __floor__(self):
        floorMatrix = []
        for i in range(self.matrix.nrow):
            floorMatrix.append([])
            for j in range(self.matrix.ncol):
                floorMatrix[i].append(math.floor(self.matrix.data[i][j]))
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=floorMatrix)

    # *------- Methods for Matrix Analysis ------------------------------------*

    # *------- Equality -------------------------------------------------------*

    def __eq__(self, matrix2):
        return self.equals(matrix2)

    def equals(self, matrix2):
        """
        Checks for equality of the two matrices
        based on dimensions and the data inside.
        Returns a Boolean Value
        """
        if (self.matrix.dimensions == matrix2.matrix.dimensions) and (
            self.matrix.data == matrix2.matrix.data
        ):
            return True
        else:
            return False

    # *------- pyrix.matrix.Matrix.isSquareMatrix() ---------------------------*

    def isSquareMatrix(self):
        """
        Checks if the Matrix is a square Matrix or not
        A square matrix is a matrix with equal number of rows and cols
        Returns a Boolean value
        """
        if self.matrix.nrow == self.matrix.ncol:
            return True
        else:
            return False

    # *------- pyrix.matrix.Matrix.isInvertible() -----------------------------*

    def isInvertible(self):
        """
        Checks if the Matrix is an Invertible Matrix or not
        An Invertible matrix is a matrix with a non zero determinant
        Returns a Boolean value
        """
        if self.matrix.singular == True and self.matrix.invertibility == False:
            return False
        if not self.isSquareMatrix():
            return False
        else:
            self.determinantValue()
            if self.matrix.determinant == 0:
                return False
            else:
                return True

    # *------- pyrix.matrix.Matrix.isSymmetricMatrix() ------------------------*

    def isSymmetricMatrix(self):
        """
        Returns a boolean value based on the matrix symmetry
        """
        if(self.matrix.symmetry):
            return self.matrix.symmetry
        assert self.isSquareMatrix(), "A Square Matrix is a Primary Requirement"
        transposeMarix = self.transposeTransform()
        transposedata = transposeMarix.matrix.data
        setattr(self, "transposedata", transposedata)
        if transposedata == self.matrix.data:
            return True
        else:
            return False
    
    # *------- pyrix.matrix.Matrix.isOrthogonalMatrix() -----------------------*

    def isOrthogonalMatrix(self):
        """
        Returns a boolean value based on the matrix Orthogonality
        """
        assert self.isSquareMatrix(), "A Square Matrix is a Primary Requirement"
        transposeMarix = self.transposeTransform()
        transposedata = transposeMarix.matrix.data
        inverseMatrix = self.invertMatrix()
        invertdata = inverseMatrix.matrix.data
        if transposedata == invertdata:
            return True
        else:
            return False

    # *------- pyrix.matrix.Matrix.copy() -------------------------------------*

    def copy(self):
        """
        Creates a DEEP(HARD) copy of the Matrix object\n
        Returns a Matrix Object
        """
        return copy.deepcopy(self)

    # *------- pyrix.matrix.Matrix.getRow() -----------------------------------*

    def getRow(self, index):
        """
        Selects a Row of the matrix of specified index\n
        Returns a list of the values
        """
        temp = [[]]
        for j in range(self.matrix.ncol):
            temp[0].append(self.matrix.data[index][j])
        s = Matrix(nrow=1, ncol=self.matrix.ncol, data=temp)
        return s

    # *------- pyrix.matrix.Matrix.getCol() -----------------------------------*

    def getCol(self, index):
        """
        Selects a Column of the matrix of specified index\n
        Returns a list(or nested list) of the values
        """
        temp = []
        for i in range(self.matrix.nrow):
            temp.append([])
            temp[i].append(self.matrix.data[i][index])
        s = Matrix(nrow=self.matrix.nrow, ncol=1, data=temp)
        return s

    # *------- pyrix.matrix.Matrix.RoundOff() ---------------------------------*

    def RoundOff(self, extent):
        """
        Rounds off the Value of the data in the matrix object to the given
        extent. Returns NoneType and should not be assigned to a variable.
        """
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                self.matrix.data[i][j] = round(self.matrix.data[i][j], extent)

    # *------- pyrix.matrix.Matrix.scaleMatrix() ------------------------------*

    def scaleMatrix(self, scalar):
        """
        Scales the Value of the data in the matrix object by the scalar value
        Returns NoneType and should not be assigned to a variable.
        """
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                self.matrix.data[i][j] *= scalar
        return self

    # *------- pyrix.matrix.Matrix.determinantValue() -------------------------*

    def determinantValue(self):
        """
        Determines the determinant value of the matrix object
        Returns int or float depending on the outcome
        """
        if self.matrix.determinant == None:
            if self.isSquareMatrix():
                determinant = self.__determinantHelper(Copy(self.matrix.data))
                self.matrix.determinant = determinant
                if determinant == 0:
                    self.matrix.invertibility = False
                    self.matrix.singular = True
                return determinant
            else:
                raise incompaitableTypeException
        else:
            return self.matrix.determinant

    # *------- pyrix.matrix.Matrix.__determinantHelper() ----------------------*

    def __determinantHelper(self, x, sum=0):
        """
        This Method specifically helps with recursive implementation of
        determinant algorithm.
        """
        count = list(range(len(x)))
        if len(x) == 2 and len(x[0]) == 2:
            v = x[0][0] * x[1][1] - x[0][1] * x[1][0]
            return v
        for i in count:
            cp = copy.deepcopy(x)
            cp = cp[1:]
            size = len(cp)
            for h in range(size):
                cp[h] = cp[h][0:i] + cp[h][i + 1 :]
            sign = pow((-1), (i % 2))
            subdet = self.__determinantHelper(cp)
            sum += x[0][i] * sign * subdet
        return sum

    # *------- pyrix.matrix.Matrix.matrixRank() -------------------------------*

    def matrixRank(self):
        """
        Calculates the Rank of the matrix object.
        Returns integer value of rank.
        """
        cself = self.copy()
        x = cself.rowEchleonTransform()
        rank = 0
        for i in range(x.matrix.nrow):
            for j in range(x.matrix.ncol):
                if x.matrix.data[i][j] == 0:
                    pass
                if x.matrix.data[i][j] != 0:
                    rank += 1
                    break
        self.matrix.rank = rank
        return rank

    # *------- pyrix.matrix.Matrix.matrixTrace() ------------------------------*

    def matrixTrace(self):
        """
        The trace of a square matrix is defined to be the sum of elements on the
        main diagonal of a Matrix. Returns a int/float value.
        """
        if(self.matrix.trace!=None):
            return self.matrix.trace
        trace = 0
        if self.isSquareMatrix():
            for i in range(self.matrix.nrow):
                trace += self.matrix.data[i][i]
        self.matrix.trace = trace
        return trace

    # *------- pyrix.matrix.Matrix.isUpperTriangularMatrix() ------------------*

    def isUpperTriangularMatrix(self):
        """
        This method determines whether a Matrix is a Upper Triangular matrix or
        not. Returns a Boolean value.
        """
        isUpperTriangularMatrix = True
        isLowerTriangularMatrix = True
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                if (i < j) and (self.matrix.data[i][j] != 0):
                    isUpperTriangularMatrix = False
                if (i > j) and (self.matrix.data[i][j] != 0):
                    isLowerTriangularMatrix = False
        if (isUpperTriangularMatrix) and (not isLowerTriangularMatrix):
            self.matrix.triangularity = 2
            return True
        else:
            return False

    # *------- pyrix.matrix.Matrix.isLowerTriangularMatirx() -------------------*

    def isLowerTriangularMatrix(self):
        """
        This method determines whether a Matrix is a Lower Triangular matrix or
        not. Returns a Boolean value.
        """
        isUpperTriangularMatrix = True
        isLowerTriangularMatrix = True
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                if (i < j) and (self.matrix.data[i][j] != 0):
                    isUpperTriangularMatrix = False
                if (i > j) and (self.matrix.data[i][j] != 0):
                    isLowerTriangularMatrix = False
        if (isLowerTriangularMatrix) and (not isUpperTriangularMatrix):
            self.matrix.triangularity = 1
            return True
        else:
            return False

    # *------- Intermatrix Row and column operations --------------------------*

    # *------- pyrix.matrix.Matrix.addRows() ----------------------------------*

    def addRows(self, index1, m2, index2):
        """
        Adds row values of one matrix to another matrix.
        Returns NoneType and should not be assigned to a variable
        """
        self.matrix.data[index1] = self.__row_add(
            self.matrix.data[index1], m2.matrix.data[index2]
        )

    # *------- pyrix.matrix.Matrix.subRows() ----------------------------------*

    def subRows(self, index1, m2, index2):
        """
        Subtracts row values of one matrix to another matrix.
        Returns NoneType and should not be assigned to a variable.
        """
        self.matrix.data[index1] = self.__row_sub(
            self.matrix.data[index1], m2.matrix.data[index2]
        )

    # *------- IntraMatrix Row and Col Operations -----------------------------*

    # *------- pyrix.matrix.Matrix.addRow() -----------------------------------*

    def addRow(self, index1, index2):
        """
        Adds row values of one matrix to same matrix.
        Returns NoneType and should not be assigned to a variable.
        """
        self.matrix.data[index1] = self.__row_add(
            self.matrix.data[index1], self.matrix.data[index2]
        )

    # *------- pyrix.matrix.Matrix.subRow() -----------------------------------*

    def subRow(self, index1, index2):
        """
        Subtracts row values of one matrix to same matrix.
        Returns NoneType and should not be assigned to a variable.
        """
        self.matrix.data[index1] = self.__row_sub(
            self.matrix.data[index1], self.matrix.data[index2]
        )

    # *------- Transformations on matrices ------------------------------------*

    # *------- pyrix.matrix.Matrix.invertMatrix() -----------------------------*

    def invertMatrix(self):
        """
        Creates an Inverse Matrix of the given matrix
        Returns a Matrix object
        """
        if self.matrix.nrow != self.matrix.ncol:
            raise incompaitableTypeException
        if self.matrix.invertibility == False:
            pass
        if getattr(self.matrix,"identityMatrix")==True:
            return self
        else:
            AM = Copy(self.matrix.data)
            IM = identityMatrix(self.matrix.nrow, self.matrix.ncol).matrix.data
            for fd in range(len(AM)):
                if AM[fd][fd] == 0:
                    AM[fd][fd] = 0.0000000000001
                fdScaler = 1.0 / AM[fd][fd]
                for j in range(len(AM)):
                    AM[fd][j] *= fdScaler
                    IM[fd][j] *= fdScaler
                for i in list(range(len(AM)))[0:fd] + list(range(len(AM)))[fd + 1 :]:
                    crScaler = AM[i][fd]
                    for j in range(len(AM)):
                        AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                        IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

            if self.__verify(IM):
                self.matrix.singular = False
                for i in range(len(IM[0])):
                    for j in range(len(IM[i])):
                        IM[i][j] = IM[i][j]
                inverteddata = IM
                return Matrix(
                    nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=inverteddata
                )
            else:
                self.matrix.determinant = 0
                self.matrix.singular = True
                raise nonInvertibleException

    # *------- pyrix.matrix.Matrix.__verify() ---------------------------------*

    def __verify(self, m2):
        """
        This method verifies a unverse of the matrix by multiplying it with the
        orignal input matrix to get identity matrix.
        """
        matrixs = []
        m1 = Copy(self.matrix.data)
        im = []
        s = 0
        l = len(m1)
        for i in range(l):
            matrixs.append([])
            im.append([])
            for j in range(l):
                if i == j:
                    im[i].append(1)
                else:
                    im[i].append(0)
                for k in range(l):
                    s += m1[i][k] * m2[k][j]
                matrixs[i].append(round(s, 1))
                s = 0

        if matrixs == im:
            return True
        else:
            return False

    # *------- pyrix.matrix.Matrix.__row_add() --------------------------------*

    def __row_add(self, row_left, row_right):
        return [a + b for (a, b) in zip(row_left, row_right)]

    # *------- pyrix.matrix.Matrix.__row_mult() -------------------------------*

    def __row_mult(self, row, num):
        return [x * num for x in row]

    # *------- pyrix.matrix.Matrix.__row_sub() --------------------------------*

    def __row_sub(self, row_left, row_right):
        return [a - b for (a, b) in zip(row_left, row_right)]

    # *------- pyrix.matrix.Matrix.__scalarDivideRow() ------------------------*

    def __scalarDivideRow(self, row, value):
        return [(x / value) for x in row]

    # *------- pyrix.matrix.Matrix.rowEchleonTransform() ----------------------*

    def rowEchleonTransform(self):
        """
        Reduces the matrix into row Echleon form.
        """
        zx = self.copy()
        temp = zx.matrix.data

        def echleonS(rw, col):
            for i, row in enumerate(temp[(col + 1) :]):
                i += 1
                if rw[col] == 0:
                    continue
                temp[i + col] = self.__row_sub(
                    row, self.__row_mult(rw, row[col] / rw[col])
                )

        for i in range(len(self.matrix.data)):
            current_row = temp[i]
            echleonS(current_row, i)
            temp = [
                [(0 if (0.0000000001 > x > -0.0000000001) else x) for x in row]
                for row in temp
            ]
        s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=temp)
        return s

    # *------- pyrix.matrix.Matrix.RrowEchleonTransform() ---------------------*

    def RrowEchleonTransform(self):
        """
        This method attempts to reduce the matrix even further than rowEchleon.
        """
        z = self.rowEchleonTransform().matrix.data
        for i in range(len(z)):
            if z[i][i] != 1:
                z[i] = self.__scalarDivideRow(z[i], z[i][i])
        if self.matrix.nrow == self.matrix.ncol:
            IM = identityMatrix(self.matrix.ncol, self.matrix.nrow)
            loopcounter=0
            while z == IM.matrix.data:
                for j in range(len(z)):
                    for i in range(len(z[0])):
                        if j == i:
                            continue
                        if z[j][i] != 0:
                            self.__row_sub(z[j], self.__row_mult(z[i], z[i][j]))
                loopcounter+=1
        s = Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=z)
        return s

    # *------- pyrix.matrix.Matrix.transposeTransform() -----------------------*

    def transposeTransform(self):
        """
        Transpose of the original matrix is created.
        Returns a Matrix Object.
        """
        c = []
        for i in range(self.matrix.ncol):
            c.append([])
            for j in range(self.matrix.nrow):
                c[i].append(self.matrix.data[j][i])
        s = Matrix(nrow=self.matrix.ncol, ncol=self.matrix.nrow, data=c)
        return s

    # *------- Supplementary Methods -----------------------------------------*

    # *------- pyrix.matrix.Matrix.vectorMultiplication() --------------------*

    def vectorMultiplication(self, v1):
        """
        Multiply a vector list with a matrix.
        """
        if self.matrix.nrow != len(v1):
            raise incompaitableTypeException
        else:
            vector = v1
            matrix = self.matrix.data
            c = []
            sum = 0
            for i in range(self.matrix.nrow):
                c.append([])
                for j in range(self.matrix.ncol):
                    sum += matrix[j][i] * vector[j]
                c[i].append(sum)
                sum = 0
            p = Matrix(ncol=1, nrow=len(v1), data=c)
            return p

    # *------- pyrix.matrix.Matrix.dotProduct() -------------------------------*

    def dotProduct(self, m2):
        """
        Performs dot product on two matrices.
        """
        sum = 0
        for row in range(self.matrix.nrow):
            for col in range(self.matrix.ncol):
                sum += self.matrix.data[row][col] * m2.matrix.data[row][col]
        return sum

    # *------- pyrix.matrix.Matrix.adjointTransform() -------------------------*

    def adjointTransform(self):
        """
        Returns the adjoint matrix of the self matrix.
        """
        cofactor = self.getAllCofactors()
        return cofactor.transposeTransform()

    # *------- pyrix.matrix.Matrix.minorSpecific() ----------------------------*

    def minorSpecific(self, row, column):
        """
        Finds a specific minor value for a certain position.
        Returns a Int/Float Value.
        """
        if self.matrix.minor == None:
            self.getAllMinors()
        else:
            pass
        return self.matrix.minor[row][column]

    # *------- pyrix.matrix.Matrix.cofactorSpecific() -------------------------*

    def cofactorSpecific(self, row, column):
        """
        Finds a specific cofactor Value of a certain position.
        Returns a Int/Float Value.
        """
        return self.getAllCofactors().matrix.data[row][column]

    # *------- pyrix.matrix.Matrix.getAllMinors() -----------------------------*

    def getAllMinors(self):
        """
        Finds all the minor values of the matrix object.
        Returns a new Matrix Object of minors.
        """
        matrixdata = Copy(self.matrix.data)
        if self.isSquareMatrix():
            if self.matrix.dimensions == [2, 2]:
                allminorslist = self.__minor2x2(matrixdata)
            else:
                allminorslist = self.__minor(matrixdata)
            self.matrix.minor = allminorslist
            return Matrix(
                nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=self.matrix.minor
            )
        else:
            raise incompaitableTypeException

    # *------- pyrix.matrix.Matrix.getAllCofactors() --------------------------*

    def getAllCofactors(self):
        """
        Finds all the cofactor values of the matrix object.
        Returns a new Matrix Object of cofactors.
        """
        if self.matrix.minor == None:
            self.getAllMinors()
        else:
            pass
        cofactors = self.__cofactor(self.matrix.minor)
        return Matrix(nrow=self.matrix.nrow, ncol=self.matrix.ncol, data=cofactors)

    # *------- pyrix.matrix.Matrix.__minor2x2() -------------------------------*

    def __minor2x2(self, matrixdata):
        """
        Finds minor values for 2x2 matrices.
        Private method
        Returns a nested list.
        """
        return [
            [matrixdata[1][1], matrixdata[1][0]],
            [matrixdata[0][1], matrixdata[0][0]],
        ]

    # *------- pyrix.matrix.Matrix.__cofactor() -------------------------------*

    def __cofactor(self, minorlist):
        """
        Finds cofactor values. A Private method.
        Returns a nested list of cofactors.
        """
        cofactors = []
        for i in range(self.matrix.nrow):
            cofactors.append([])
            for j in range(self.matrix.ncol):
                cofactors[i].append(minorlist[i][j] * pow(-1, i + j + 2))
        return cofactors

    # *------- pyrix.matrix.Matrix.__minor() ----------------------------------*

    def __minor(self, matrixdata):
        """
        Finds minor values. A Private method.
        Returns a nested list of minors.
        """
        minors = []
        for i in range(len(matrixdata)):
            minors.append([])
            for j in range(len(matrixdata[0])):
                minors[i].append(
                    self.__determinantHelper(self.__matrixsplitter(matrixdata, i, j))
                )
        return minors

    # *------- pyrix.matrix.Matrix.__matrixsplitter() -------------------------*

    def __matrixsplitter(self, matrixdata, exceptionrow, exceptioncol):
        """
        Splits the matrix into a smaller matrix excluding the exceptionrow and
        exceptioncolumn.
        """
        excludedmatrix = []
        returnmatrix = []
        iterator = 0
        for i in range(len(matrixdata)):
            for j in range(len(matrixdata[i])):
                if [i, j] == [exceptionrow, j]:
                    continue
                if [i, j] == [i, exceptioncol]:
                    continue
                else:
                    excludedmatrix.append(matrixdata[i][j])
                    iterator += 1
        dimensions = math.sqrt(len(excludedmatrix))
        for i in range(int(dimensions)):
            returnmatrix.append([])
            returnmatrix[i] = excludedmatrix[0 : int(dimensions)]
            del excludedmatrix[0 : int(dimensions)]
        return returnmatrix

    # *------- pyrix.matrix.Matrix.__unlistifydata() --------------------------*

    def __unlistifydata(self, data, rowcount, colcount):
        """
        converts a single listed matrix into nested listed matrix.
        """
        clist = self.copy().matrix.data
        return __nestifyMatrix(clist, rowcount, colcount)

    # *------- Statistical Methods --------------------------------------------*

    # *------- pyrix.matrix.Matrix.glovalMean() -------------------------------*

    def globalMean(self):
        """
        This method finds the mean value in the whole matrix\n
        Returns a int/float value of mean.
        """
        data = self.matrix.data
        count = 0
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                count += data[i][j]
        return count / (self.matrix.nrow * self.matrix.ncol)

    # *------- pyrix.matrix.Matrix.localRowMean() -----------------------------*

    def localRowMean(self, rowindex):
        """
        This method finds the mean value in the indexed row of the matrix\n
        Returns the mean of the selected row.
        """
        data = self.matrix.data
        count = 0
        for i in range(len(data[rowindex])):
            count += data[rowindex][i]
        return count / self.matrix.nrow

    # *------- pyrix.matrix.Matrix.localColumnMean() --------------------------*

    def localColumnMean(self, colindex):
        """
        This method finds the mean value in the indexed column of the matrix\n
        Returns the mean of the selected column.
        """
        data = self.matrix.data
        count = 0
        for i in range(len(data[colindex])):
            count += data[i][colindex]
        return count / self.matrix.ncol

    # *------- pyrix.matrix.Matrix.globalMedian() -----------------------------*
    
    def globalMedian(self):
        """
        This method finds the median value in the whole matrix\n
        Returns a int/float value of median.
        """
        globalmedian = None
        serializeddata = listifyMatrix(self.matrix.data)
        serializeddata.sort()
        if len(serializeddata) % 2 != 0:
            globalmedian = serializeddata[int((-1 + len(serializeddata)) / 2)]
        else:
            globalmedian = serializeddata[int(math.ceil(len(serializeddata) / 2))]
        return globalmedian

    # *------- pyrix.matrix.Matrix.localRowMedian() ---------------------------*

    def localRowMedian(self, rowindex):
        """
        This method finds the median value in the indexed row of the matrix\n
        Returns the median of the selected row.
        """
        localmedian = None
        localrow = self.matrix.data[rowindex]
        localrow.sort()
        if len(localrow) % 2 != 0:
            localmedian = localrow[int((-1 + len(localrow)) / 2)]
        else:
            localmedian = localrow[int(math.ceil(len(localrow) / 2))]
        return localmedian

    # *------- pyrix.matrix.Matrix.localColumnMedian() ------------------------*

    def localColumnMedian(self, colindex):
        """
        This method finds the median value in the indexed column of the matrix\n
        Returns the median of the selected column
        """
        localmedian = None
        localcol = [z[colindex] for z in self.matrix.data]
        localcol.sort()
        if len(localcol) % 2 != 0:
            localmedian = localcol[int((-1 + len(localcol)) / 2)]
        else:
            localmedian = localcol[int(math.ceil(len(localcol) / 2))]
        return localmedian

    # *------- pyrix.matrix.Matrix.globalMode() -------------------------------*

    def globalMode(self):
        """
        This method finds the mode value in the whole matrix\n
        Returns a int/float value of mode.
        """
        globalcount = dict()
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                currentVal = self.matrix.data[i][j]
                if currentVal not in globalcount:
                    globalcount[currentVal] = 1
                else:
                    globalcount[currentVal] += 1
        return max(globalcount, key=globalcount.get)

    # *------- pyrix.matrix.Matrix.localRowMode() -----------------------------*

    def localRowMode(self, rowindex):
        """
        This method finds the mode value in the indexed row of the matrix\n
        Returns the mode of the selected row
        """
        localcount = dict()
        for i in range(self.matrix.ncol):
            currentVal = self.matrix.data[rowindex][i]
            if currentVal not in localcount:
                localcount[currentVal] = 1
            else:
                localcount[currentVal] += 1
        return max(localcount, key=localcount.get)

    # *------- pyrix.matrix.Matrix.localColumnMode() --------------------------*

    def localColumnMode(self, colindex):
        """
        This method finds the mode value in the indexed column of the matrix\n
        Returns the mode of the selected column
        """
        localcount = dict()
        for i in range(self.matrix.nrow):
            currentVal = self.matrix.data[i][colindex]
            if currentVal not in localcount:
                localcount[currentVal] = 1
            else:
                localcount[currentVal] += 1
        return max(localcount, key=localcount.get)

    __repr__ = __str__

# *------- pyrix.matrix.listifyMatrix() ---------------------------------------*

def listifyMatrix(MatrixObjectdata):
    """
    This function returns a single list of all values in the matrix object's
    nested list structure.
    """
    matrixdata = MatrixObjectdata
    listifiedmatrix = []
    for i in range(len(MatrixObjectdata)):
        for j in range(len(MatrixObjectdata[i])):
            listifiedmatrix.append(matrixdata[i][j])
    return listifiedmatrix

# *------- pyrix.matrix.__nestifyMatrix() -------------------------------------*

def __nestifyMatrix(listeddata, rowcount, colcount):
    """
    Performs the inverse function of listifymatrix() method. 
    """
    clist = listeddata
    nested = []
    for i in range(rowcount):
        nested.append(clist[i:colcount])
        del clist[i:colcount]
    return nested


# Quick Initialization  Methods

# *------- pyrix.matrix.Copy() ------------------------------------------------*

def Copy(AnyObject):
    """
    Returns A Deep copy of the object
    """
    return copy.deepcopy(AnyObject)


# *------- pyrix.matrix.zeroMatrix() ------------------------------------------*

def zeroMatrix(nrow, ncol):
    """
    Create a zero matrix of the given dimensions.
    Retuns a Matrix Object.
    """
    t = []
    for i in range(nrow):
        t.append([])
        for _j in range(ncol):
            t[i].append(0)
    s = Matrix(nrow=nrow, ncol=ncol, data=t)
    if(nrow == ncol):
        s.matrix.symmetry = True
        s.matrix.trace=0
    return s

# *------- pyrix.matrix.unitMatrix() ------------------------------------------*

def unitMatrix(nrow, ncol):
    """
    Create a unit matrix of the given dimensions.
    Retuns a Matrix Object.
    """
    t = []
    for i in range(nrow):
        t.append([])
        for _j in range(ncol):
            t[i].append(1)
    s = Matrix(nrow=nrow, ncol=ncol, data=t)
    if(nrow==ncol):
        s.matrix.symmetry=True
        s.matrix.trace=nrow
    return s

# *------- pyrix.matrix.identityMatrix() --------------------------------------*

def identityMatrix(nrow, ncol):
    """
    Create a identity matrix of the given dimensions
    Works for square Matrices
    Retuns a Matrix Object
    """
    if nrow == ncol:
        t = []
        for i in range(nrow):
            t.append([])
            for j in range(ncol):
                if i == j:
                    t[i].append(1)
                else:
                    t[i].append(0)
        s = Matrix(nrow=nrow, ncol=ncol, data=t)
        s.matrix.symmetry=True
        s.matrix.trace=nrow
        s.matrix.invertibility=True
        setattr(s.matrix,"identityMatrix",True)
        return s
    else:
        raise incompaitableTypeException

# *------- pyrix.matrix.randomMatrix() ----------------------------------------*

def randomMatrix(scale, type):
    """
    Generates a pseudo random matrix of a given scale(small,large) and 
    datatype(float/int).
    """
    if scale == "small" and type == "int":
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.randint(1, 100))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if scale == "large" and type == "int":
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.randint(10, 10000))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s

    if scale == "small" and type == "float":
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.triangular(low=0.0, high=10.0))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if scale == "large" and type == "float":
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.triangular(low=0.0, high=1000.0))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
