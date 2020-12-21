#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/Vector\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : An extension to pyrix for vectors\n
Encoding    : UTF-8\n
Version     :0.7.19\n
Build       :0.7.19/21-12-2020
"""
#*------- Imports -------------------------------------------------------------*
from pyrix.exception import (
    incompaitableTypeException,
    divisionErrorException,
    bitWiseOnMatrix,
)  # exceptions required
import math  # for basic math functions
import copy  # for deep copy()
import random  # for random matrix
#*-----------------------------------------------------------------------------*

#*------- pyrix.vector.vectorData ---------------------------------------------*

class vectorData(object):
    """
    All The Vector Data is stored here which allows for implementing Dynamic
    Programming Principles such as Memoization:\n
    Data List:
        1.dimensions[int]:The number of dimensions of a vector is represented.
        2.data[list]: The vector data is stored here.
        3.ncol[int]: Number of Columns
        4.directionVectorSet[list]: list of direction Vector Objects
    (Not Implemented yet)
        5.classType:defines the type of pyrix/vector implementation
    (occours in inheriting classes)
    """

    def __init__(self, dims, data):
        self.data = data
        self.dimensions = dims
        self.directionVectorSet = None
        self.ncol = dims
        self.classType = "Vector"

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            raise AttributeError(key)

    def __delattr__(self, key):
        del self.__dict__[key]

#*------- pyrix.vector.Vector -------------------------------------------------*

class Vector:
    """
    Get Started By Creating a Vector Object\n
        dims=number of dimensions\n
        data=corresponding vector data of the dimensions as a list\n
        eg. Vect = Vector(dims=2,data=[1,1])
    """

    def __init__(self, dims, data):
        self.vector = vectorData(dims, data)

    def __str__(self):
        stringV = str()
        stringV = "Vector:\n"
        for item in self.vector.data:
            stringV += str(item) + "\n"
        stringV += "Dimensions :" + str(self.vector.dimensions)
        return stringV

    def __repr__(self):
        pass
    
    __repr__ = __str__
    #*------- Add Vectors -----------------------------------------------------*

    def __add__(self, Vector2):
        if self.vector.dimensions == Vector2.vector.dimensions:
            sum = []
            for i in range(self.vector.dimensions):
                sum.append(self.vector.data[i] + Vector2.vector.data[i])
            return Vector(dims=self.vector.dimensions, data=sum)
        else:
            raise incompaitableTypeException


    #*------- Subtract Vectors ------------------------------------------------*

    def __sub__(self, Vector2):
        if self.vector.dimensions == Vector2.vector.dimensions:
            diff = []
            for i in range(self.vector.dimensions):
                diff.append(self.vector.data[i] - Vector2.vector.data[i])
            return Vector(dims=self.vector.dimensions, data=diff)
        else:
            raise incompaitableTypeException

    #*------- Multiply Vectors ------------------------------------------------*

    def __mul__(self, Vector2):
        print(
            "Depending on the application use other methods like:\n \
                1. dotProduct\n \
                2. crossProduct(Under-Development) \
            "
        )

    #*------- TrueDivision Vectors --------------------------------------------*
    
    def __truediv__(self, m2):
        raise divisionErrorException

    #*------- Equality Vectors ------------------------------------------------*

    def __eq__(self, vector2):
        if (self.vector.dimensions == vector2.vector.dimensions) and (
            self.vector.data == vector2.vector.data
        ):
            return True
        else:
            return False

    #*------- Floor Division Vectors ------------------------------------------*

    def __floordiv__(self, m2):
        raise divisionErrorException

    #*------- Modulus Vectors -------------------------------------------------*

    def __mod__(self, m2):
        raise divisionErrorException

    #*------- lshift << Vectors -----------------------------------------------*

    def __lshift__(self, m2):
        raise bitWiseOnMatrix

    #*------- rshift >> Vectors -----------------------------------------------*

    def __rshift__(self, m2):
        raise bitWiseOnMatrix

    #*------- AND & Vectors ---------------------------------------------------*

    def __and__(self, m2):
        raise bitWiseOnMatrix

    #*------- OR | Vectors ----------------------------------------------------*

    def __or__(self, m2):
        raise bitWiseOnMatrix

    #*------- XOR ^ Vectors ---------------------------------------------------*

    def __xor__(self, m2):
        raise bitWiseOnMatrix

    #*------- INVERT ~ Vectors ------------------------------------------------*

    def __invert__(self):
        raise bitWiseOnMatrix

    #*------- Absolute Vectors ------------------------------------------------*

    def __abs__(self):
        return self.vectorNorm()

    #*------- Power ** Vectors ------------------------------------------------*

    def __pow__(self, scalar):
        return self.dotProduct(v2=self)

    #*------- pyrix.vector.Vector.copy() --------------------------------------*

    def copy(self):
        """
        Returns a deep copy of self.
        """
        return copy.deepcopy(self)

    #*------- pyrix.vector.Vector.dotProduct() --------------------------------*

    def dotProduct(self, v2):
        """
        Performs dot product with another vector.
        """
        assert (
            self.vector.dimensions == v2.vector.dimensions
        ), "incompaitableTypeException"
        dotproduct = 0
        for i in range(self.vector.dimensions):
            dotproduct += (self.vector.data[i]) * (v2.vector.data[i])
        return dotproduct

    #*------- pyrix.vector.Vector.vectorNorm() --------------------------------*

    def vectorNorm(self):
        """
        Calculates the vector norm.
        """
        norm = math.sqrt(self.dotProduct(v2=self))
        return norm

    #*------- pyrix.vector.Vector.vectorNormalize() ---------------------------*

    def vectorNormalize(self):
        """
        Normalizes the vector with vector norm value.
        """
        normValue = self.vectorNorm()
        assert normValue != 0, "Vector normal value 0"
        for i in range(self.vector.dimensions):
            self.vector.data[i] /= normValue
        return self

    #*------- pyrix.vector.Vector.scaleVector() -------------------------------*

    def scaleVector(self, scalar):
        """
        Scales the vector with a scalar value.
        """
        data = self.vector.data
        for i in range(self.vector.dimensions):
            data[i] *= scalar
        return self

    #*------- pyrix.vector.Vector.crossProduct() ------------------------------*

    def crossProduct(self, v2):
        raise NotImplementedError

    #*------- pyrix.vector.Vector.orthogonalityVector() -----------------------*

    def orthogonalityVector(self):
        raise NotImplementedError

    __repr__ == __str__

#*------- pyrix.vector.unitVector() -------------------------------------------*

def unitVector(dims):
    """
    Generates a vector with 1 as values of n dimensions.
    """
    VectorData = []
    for _i in range(dims):
        VectorData.append(1)
    return Vector(dims=dims, data=VectorData)

#*------- pyrix.vector.zeroVector() -------------------------------------------*

def zeroVector(dims):
    """
    Generates a vector with 0 as values of n dimensions.
    """
    VectorData = []
    for _i in range(dims):
        VectorData.append(0)
    return Vector(dims=dims, data=VectorData)

#*------- pyrix.vector.randomVector() -----------------------------------------*

def randomVector(scale, type):
    """
    Generates a pseudo random vector of a given scale(small,large) and 
    datatype(float/int).
    """
    if scale == "small" and type == "int":
        dims = random.randint(1, 10)
        data = []
        for _i in range(dims):
            data.append(random.randint(1, 100))
        s = Vector(dims=dims, data=data)
        return s
    if scale == "large" and type == "int":
        dims = random.randint(10, 100)
        data = []
        for _i in range(dims):
            data.append(random.randint(10, 10000))
        s = Vector(dims=dims, data=data)
        return s

    if scale == "small" and type == "float":
        dims = random.randint(1, 10)
        data = []
        for _i in range(dims):
            data.append(random.triangular(low=0.0, high=10.0))
        s = Vector(dims=dims, data=data)
        return s
    if scale == "large" and type == "float":
        dims = random.randint(10, 100)
        data = []
        for _i in range(dims):
            data.append(random.triangular(low=0.0, high=1000.0))
        s = Vector(dims=dims, data=data)
        return s

#*------- pyrix.vector.linearVector() -----------------------------------------*

def linearVector(dims, minVal, maxVal):
    """
    generates a linear vector with min val to max val in the appropriate steps.
    """
    assert minVal <= maxVal
    "Not suitable Range"
    assert dims > 1
    "Dimensions too small"
    data = []
    gap = (maxVal - minVal) / (dims - 1)
    for i in range(dims):
        data.append(minVal + gap * i)
    linVector = Vector(dims=dims, data=data)
    return linVector

#*------- pyrix.vector.Copy() -------------------------------------------------*

def Copy(AnyObject):
    """
    Returns a deep copy of the object.
    """
    return copy.deepcopy(AnyObject)
