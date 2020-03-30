#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------ Brief Documentation --------------------
Author      : Abhishek Ulayil
Contents    : 3 Exceptions , 2 classes , 25 methods
Description : A simple matrix manipulation library  
Encoding    : UTF-8
Version     : 0.3.21
------------------------------------------------------------
"""
import sys
import copy


class divisionErrorException(Exception):
    pass


class incompaitableTypeException(Exception):
    pass

class nonInvertibleException(Exception):
    pass
class matrixData(object):
    def __init__(self,nrow,ncol,data):
        self.__dict__['nrow'] = nrow
        self.__dict__['ncol'] = ncol
        self.__dict__['dimensions'] = [nrow,ncol]
        self.__dict__['data'] = data
        self.__dict__['invertibility'] = None
        self.__dict__['determinant'] = None
        self.__dict__['singular'] = None
        self.__dict__['eigenvals'] = []
        self.__dict__['eigenvects'] = []
        self.__dict__['rank'] = None

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        return self.__dict__[key]

    def __delattr__(self, key):
        del self.__dict__[key]


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

    def __mul__(self, m2):
        if (self.matrix.ncol!=m2.matrix.nrow):
            raise divisionErrorException
        else:
            m3=[[0 for x in range(m2.matrix.ncol)] for y in range(self.matrix.nrow)]
            sum=0
            for i in range(self.matrix.nrow):
                for j in range(m2.matrix.ncol):
                    for k in range(self.matrix.ncol):
                        sum += self.matrix.data[i][k]*m2.matrix.data[k][j]
                    m3[i][j]=sum
                sum=0
        s=Matrix(nrow=self.matrix.nrow,ncol=m2.matrix.ncol,data=m3)
        return s

    def __div__(self, m2):
        raise divisionErrorException

    def __eq__(self, m2):
        if((self.matrix.dimensions == m2.matrix.dimensions)and(self.matrix.data == m2.matrix.data)):
            return True
        else:
            return False

    def __floordiv__(self, m2):
        raise divisionErrorException

    def invertMatrix(self):
        if(self.matrix.nrow!=self.matrix.ncol):
            raise incompaitableTypeException
        else:
            AM=self.matrix.data
            IM=identityMatrix(self.matrix.nrow,self.matrix.ncol).matrix.data
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
                self.matrix.singular=False
                for i in range(len(IM[i])):
                    for j in range(len(IM[i])):
                        IM[i][j] = round(IM[i][j], 2)
                self.matrix.data=IM
            else:
                self.matrix.determinant=0
                self.matrix.singular=True
                raise nonInvertibleException
    def verify(self, m2):
        matrixs = []
        m1=self.matrix.data
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
        
        if(matrixs==im):
            return True
        else:
            return False

    def rowEchleonTransform(self):
        pass

    def RrowEchleonTransform(self):
        pass

    def copy(self):
        return copy.deepcopy(self)

    def transposeTransform(self):
        pass

    def vectorMultiplication(self, v1):
        pass

    def scaleMatrix(self, scalar):
        for i in range(self.matrix.nrow):
            for j in range(self.matrix.ncol):
                self.matrix.data[i][j]*=scalar

    def determinantValue(self):
        pass
    def matrixRank(self):
        pass

    def strassenMultiplication(self, m2):
        pass

    def eigenTerms(self):
        pass

    __repr__ = __str__


def zeroMatrix(nrow, ncol):
    t = []
    for i in range(nrow):
        t.append([])
        for j in range(ncol):
            t[i].append(0)
    s = Matrix(nrow=nrow, ncol=ncol, data=t)
    return s

def identityMatrix(nrow,ncol):
    if(nrow==ncol):
        t=[]
        for i in range(nrow):
            t.append([])
            for j in range(ncol):
                if(i==j):
                    t[i].append(1)
                else:
                    t[i].append(0)
        s=Matrix(nrow=nrow,ncol=ncol,data=t)
        return s
    else:
        raise incompaitableTypeException
