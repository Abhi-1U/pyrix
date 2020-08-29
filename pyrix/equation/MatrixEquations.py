#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/MatrixEquations\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : An extension for matrix Based Equations \n
Encoding    : UTF-8\n
Version     :0.7.16rc0\n
Build       :0.7.16rc0/29-08-2020
"""
from pyrix.binarymatrix.binarymatrix import BinaryMatrix
from pyrix.matrix.Matrix import Matrix


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


class MEquation(BinaryMatrix):
    def ACRTransform(self):
        pass

    def ALUTransform(self):
        pass

    def AQRTransform(self):
        pass

    def augmentedMatrix(self):
        pass

    def singularValue(self):
        pass

    def LUdecomposition(self):
        pass

    def eigenTerms(self):
        pass

    def orthogonaleigenVectors(self):
        pass

    def JordanGuassElimination(self):
        pass
