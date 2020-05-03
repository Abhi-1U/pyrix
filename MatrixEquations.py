#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Name        : Pyrix/MatrixEquations\n
Author      : Abhishek Ulayil\n
Contents    : 2 Exceptions Classes , 1 Function classes , 10 methods\n
Description : Am extension for matrix Based Equations \n
Encoding    : UTF-8\n
Version     : 0.0.1
--------------------------------------------------------------------
"""
from Matrix import Matrix, matrixData


class matrixEquation:
    def __init__(self, Lhs, Rhs, Nterms):
        self.lhs = Lhs
        self.rhs = Rhs
        self.nterms = Nterms

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            raise AttributeError(key)

    def __delattr__(self, key):
        del self.__dict__[key]


class MEquation(Matrix):
    def ALUTransform(self):
        pass

    def augmentedMatrix(self):
        pass

    def LUdecomposition(self):
        pass

    def JordanGuassElimination(self):
        pass
