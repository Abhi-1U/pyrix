#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/BinaryMatrix\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : A Binary matrix manipulation library  \n
Encoding    : UTF-8\n
Version     :0.7.19\n
Build       :0.7.19/21-12-2020
"""

#*------- Imports -------------------------------------------------------------*

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

#*------- pyrix.binarymatrix.BinaryMatrix -------------------------------------*

class BinaryMatrix(Matrix):
    """
    A completely Innovative approach to Matrices with Binary numbers.
    Full Logic control with Matrix types.
    Can be used as comparators,Inverters,Bit Data Manipulators as a matrix.
    BinaryMatrix.__init__() :>
    """

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

    # *------- Add BinaryMatrix -----------------------------------------------*

    def __add__(self, BinaryMat2):
        if(not BinaryMat2.isBinaryMatrix()):
            raise incompaitableTypeException
        sum = zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
        for i in range(0,self.matrix.nrow):
            for j in range(0,self.matrix.ncol):
                sum.matrix.data[i][j]=(self.matrix.data[i][j]+BinaryMat2.matrix.data[i][j])%2
        return sum

    # *------- Subtract BinaryMatrix ------------------------------------------*

    def __sub__(self, BinaryMat2):
        if(not BinaryMat2.isBinaryMatrix()):
            raise incompaitableTypeException
        sum = zeroBinaryMatrix(self.matrix.nrow, self.matrix.ncol)
        for i in range(0, self.matrix.nrow):
            for j in range(0, self.matrix.ncol):
                sum.matrix.data[i][j]=(self.matrix.data[i][j]-BinaryMat2.matrix.data[i][j])%2
        return sum


    # *------- Left Shift BinaryMatrix ----------------------------------------*

    def __lshift__(self, bits):
        if(self.matrix.bitwidth==1):
            return self.logicalShift(direction="left", bits=bits)

    # *------- Right Shift BinaryMatrix ---------------------------------------*

    def __rshift__(self, bits):
        if(self.matrix.bitwidth==1):
            return self.logicalShift(direction="Right", bits=bits)

    # *------- pyrix.binarymatrix.BinaryMatrix.isBinaryMatrix() ---------------*

    def isBinaryMatrix(self):
        """
        This method checks if the BinaryMatrix or Matrix in question is a
        Binary Matrix anymore. Works Best for Emulated Binary Mode(EBM).
        Returns Boolean True or False
        """
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

    # *------- BOOLEAN AND ----------------------------------------------------*

    def __and__(self, m2):
        return self.And(m2)

    # *------- pyrix.binarymatrix.BinaryMatrix.And() --------------------------*

    def And(self,m2):
        """
        Boolean AND implementation.
        """
        self.isBinaryMatrix()
        m2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and m2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == m2.matrix.dimensions):
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            self.__AndS(self.matrix.data[i][j],
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
    # *------- BOOLEAN OR -----------------------------------------------------*

    def __or__(self, m2):
        return self.Or(m2)
    
    # *------- pyrix.binarymatrix.BinaryMatrix.Or() ---------------------------*

    def Or(self,m2):
        """
        Boolean OR implementation.
        """
        self.isBinaryMatrix()
        m2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and m2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == m2.matrix.dimensions):
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            self.__Or(self.matrix.data[i][j],
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

    # *------- BOOLEAN XOR ----------------------------------------------------*

    def __xor__(self, m2):
        return self.ExOr(m2)

    # *------- pyrix.binarymatrix.BinaryMatrix.ExOr() -------------------------*

    def ExOr(self,m2):
        """
        Boolean EXclusive OR implementation.
        """
        self.isBinaryMatrix()
        m2.isBinaryMatrix()
        if(self.matrix.binaryMatrix == True and m2.matrix.binaryMatrix == True):
            if(self.matrix.dimensions == m2.matrix.dimensions):
                data = []
                for i in range(self.matrix.nrow):
                    data.append([])
                    for j in range(self.matrix.ncol):
                        data[i].append(
                            self.__Exor(self.matrix.data[i][j],
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

    # *------- BOOLEAN INVERT -------------------------------------------------*

    def __invert__(self):
        return self.Not()

    # *------- pyrix.binarymatrix.BinaryMatrix.Not() --------------------------*

    def Not(self):
        """
        Boolean NOT(invert) implementation.
        """
        self.isBinaryMatrix()

        if(self.matrix.binaryMatrix == True):
            data = []
            for i in range(self.matrix.nrow):
                data.append([])
                for j in range(self.matrix.ncol):
                    data[i].append(
                        self.__Not(self.matrix.data[i][j]))
            return BinaryMatrix(
                nrow=self.matrix.nrow,
                ncol=self.matrix.ncol,
                data=data
            )
        else:
            raise binaryMatrixException

    # *------- pyrix.binarymatrix.BinaryMatrix.onesComplement() ---------------*

    def onesComplement(self):
        """
        Boolean Ones Complement.
        """
        return self.__invert__()

    # *------- pyrix.binarymatrix.BinaryMatrix.twosComplement() ---------------*

    def twosComplement(self):
        """
        Boolean Twos Complement.
        """
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

    # *------- pyrix.binarymatrix.BinaryMatrix.__forward_one() ----------------*

    def __forward_one(self, data, rowcount, colcount):
        for _i in range(rowcount-1, 0, -1):
            for _j in range(colcount-1, 0, -1):
                if(data[_i][_j] == 1):
                    data[_i][_j] == 0
                    continue
                if(data[_i][_j] == 0):
                    data[_i][_j] == 1
        return data

    # *------- pyrix.binarymatrix.BinaryMatrix.Nand() -------------------------*

    def Nand(self, Bmatrix2):
        """
        Boolean NAND implementation.
        """
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
                            self.__Nand(self.matrix.data[i][j],
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

    # *------- pyrix.binarymatrix.BinaryMatrix.Nor() --------------------------*

    def Nor(self, Bmatrix2):
        """
        Boolean NOR implementation.
        """
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
                            self.__Nor(self.matrix.data[i][j],
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

    # *------- pyrix.binarymatrix.BinaryMatrix.ExNor() ------------------------*

    def ExNor(self, Bmatrix2):
        """
        Boolean ExNor implementation.
        """
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
                            self.__EXNor(self.matrix.data[i][j],
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

    # *------- pyrix.binarymatrix.BinaryMatrix.logicalShift() -----------------*

    def logicalShift(self, direction, bits):
        """
        Logical Shift in the specified direction and count of bits.
        """
        dataArray = self.__listifyMatrix(self)
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
        return BinaryMatrix(nrow=self.nrow,
                            ncol=self.ncol, data=dataArray)

    # *------- pyrix.binarymatrix.BinaryMatrix.circularShift() ----------------*

    def circularShift(self, direction, bits):
        """
        Circular shift implementation in the specified direction and bits.
        """
        dataArray = self.__listifyMatrix(self)
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
        return BinaryMatrix(nrow=self.nrow,
        ncol=self.ncol,data=dataArray)

    # *------- pyrix.binarymatrix.BinaryMatrix.arithmeticShift() --------------*

    def arithmeticShift(self, direction, bits):
        """
        Arithmetic shift implementation in the specified direction and bits.
        """
        dataArray = self.__listifyMatrix(self)
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
        return BinaryMatrix(nrow=self.nrow,
                            ncol=self.ncol, data=dataArray)

    # *------- pyrix.binarymatrix.BinaryMatrix.popcount() ---------------------*

    def popcount(self):
        """
        popcount will return the count of nonzero elements.
        """
        popcount = 0
        dataArray = self.__listifyMatrix(self)
        for value in dataArray:
            if (value != 0):
                popcount += 1
            else:
                continue
        return popcount

    # *------- pyrix.binarymatrix.BinaryMatrix.__Exor() -----------------------*

    def __Exor(self,t1, t2):
        if(t1 == t2):
            return 0
        else:
            return 1

    # *------- pyrix.binarymatrix.BinaryMatrix.__AndS() -----------------------*

    def __AndS(self,t1, t2):
        if(t1 == t2 == 1):
            return 1
        else:
            return 0

    # *------- pyrix.binarymatrix.BinaryMatrix.__Or() -------------------------*

    def __Or(self,t1, t2):
        if(t1 == t2 == 0):
            return 0
        else:
            return 1

    # *------- pyrix.binarymatrix.BinaryMatrix.__Nor() ------------------------*

    def __Not(self,t1):
        if(t1 == 1):
            return 0
        else:
            return 1

    # *------- pyrix.binarymatrix.BinaryMatrix.__Nand() -----------------------*

    def __Nand(self,t1, t2):
        if(t1 == t2 == 1):
            return 0
        else:
            return 1

    # *------- pyrix.binarymatrix.BinaryMatrix.__Nor() ------------------------*

    def __Nor(self,t1, t2):
        if(t1 == t2 == 0):
            return 1
        else:
            return 0

    # *------- pyrix.binarymatrix.BinaryMatrix.__EXNor() ----------------------*

    def __EXNor(self,t1, t2):
        if(t1 == t2):
            return 1
        else:
            return 0

    # *------- pyrix.binarymatrix.__listifyMatrix() -------------------------------*

    def __listifyMatrix(self,BinaryMatrixObject):
        matrixdata = BinaryMatrixObject.matrix.data
        listifiedmatrix = []
        for i in range(BinaryMatrixObject.matrix.nrow):
            for j in range(BinaryMatrixObject.matrix.ncol):
                listifiedmatrix.append(matrixdata[i][j])
        BinaryMatrixObject.matrix.listifieddata = listifiedmatrix
        return listifiedmatrix

# *------- pyrix.binarymatrix.zeroBinaryMatrix() ------------------------------*

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

# *------- pyrix.binarymatrix.unitBinaryMatrix() ------------------------------*

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

# *------- pyrix.binarymatrix.identityBinaryMatrix() --------------------------*

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

# *------- pyrix.binarymatrix.randomBinaryMatrix() ----------------------------*

def randomBinaryMatrix(scale, type):
    """
    Generates a pseudo random BinaryMatrix of a given scale(small,large) and 
    datatype(int).
    """
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

# *------- pyrix.binarymatrix.Copy() ------------------------------------------*

def Copy(AnyObject):
    """
    Returns A Deep copy of the object
    """
    return copy.deepcopy(AnyObject)
