#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
------------------------ Brief Documentation -----------------------
Name        : Pyrix/Utilities\n
Author      : Abhishek Ulayil\n
Description : Utility Extention to pyrix  \n
Encoding    : UTF-8
--------------------------------------------------------------------
"""
from binMat import Matrix, BinaryMatrix, binaryMatrixException, incompaitableTypeException
import random
import json
import csv

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
        for _j in range(ncol):
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
        for _j in range(ncol):
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
            for _j in range(ncol):
                data[i].append(random.randint(1, 100))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if(scale == "large" and type == "int"):
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.randint(10, 10000))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s

    if(scale == "small" and type == "float"):
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.triangular(low=0.0, high=10.0))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if(scale == "large" and type == "float"):
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.triangular(low=0.0, high=1000.0))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s


def zeroBinaryMatrix(nrow, ncol):
    """Create a zero Binary matrix of the given dimensions\n
        Retuns a BinaryMatrix Object
    """
    t = []
    for i in range(nrow):
        t.append([])
        for _j in range(ncol):
            t[i].append(0)
    s = BinaryMatrix(nrow=nrow, ncol=ncol, data=t)
    return s

# unitBinaryMatrix
# Creates a Binary Matrix with ones of given size and shape


def unitBinaryMatrix(nrow, ncol):
    """Create a Unit Binary matrix of the given dimensions\n
        Retuns a BinaryMatrix Object
    """
    t = []
    for i in range(nrow):
        t.append([])
        for _j in range(ncol):
            t[i].append(1)
    s = BinaryMatrix(nrow=nrow, ncol=ncol, data=t)
    return s
# identityBinaryMatrix
# Creates a Binarymatrix with zeros of given shape and size


def identityBinaryMatrix(nrow, ncol):
    """Create a identity Binary matrix of the given dimensions\n
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
        s = BinaryMatrix(nrow=nrow, ncol=ncol, data=t)
        return s
    else:
        raise incompaitableTypeException


def randomBinaryMatrix(scale, type):
    if(scale == "small" and type == "int"):
        nrow = random.randint(1, 10)
        ncol = random.randint(1, 10)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.randint(0, 1))
        s = Matrix(nrow=nrow, ncol=ncol, data=data)
        return s
    if(scale == "large" and type == "int"):
        nrow = random.randint(10, 100)
        ncol = random.randint(10, 100)
        data = []
        for i in range(nrow):
            data.append([])
            for _j in range(ncol):
                data[i].append(random.randint(0, 1))
        s = BinaryMatrix(nrow=nrow, ncol=ncol, data=data)
        return s


def reDimensionalize(AnyMatrixObject, nrow, ncol):
    listifieddata = __listifyMatrix(AnyMatrixObject)
    matrixdata = []
    for i in range(nrow):
        matrixdata.append([])
        matrixdata[i] = listifieddata[0:ncol]
        del listifieddata[0:ncol]
    if(AnyMatrixObject.matrix.classType == "Matrix"):
        return Matrix(nrow=nrow, ncol=ncol, data=matrixdata)
    if(AnyMatrixObject.matrix.classType == "BinaryMatrix"):
        return BinaryMatrix(nrow=nrow, ncol=ncol, data=matrixdata)


def __listifyMatrix(MatrixObject):
    matrixdata = MatrixObject.matrix.data
    listifiedmatrix = []
    for i in range(MatrixObject.matrix.nrow):
        for j in range(MatrixObject.matrix.ncol):
            listifiedmatrix.append(matrixdata[i][j])
    MatrixObject.matrix.listifieddata = listifiedmatrix
    return listifiedmatrix


def __nestifyMatrix(listeddata, rowcount, colcount):
    clist = listeddata
    nested = []
    for i in range(rowcount):
        nested.append(clist[i:colcount])
        del clist[i:colcount]
    return nested


def flipDimensions(AnyMatrixObject):
    newcol = AnyMatrixObject.matrix.nrow
    newrow = AnyMatrixObject.matrix.ncol
    return reDimensionalize(AnyMatrixObject, newrow, newcol)


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
        outfile.close()
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
    if classtype == 'BinaryMatrix':
        returnMatrix = BinaryMatrix(nrow=nrow, ncol=ncol, data=data)
        for key, item in object.items():
            setattr(returnMatrix.matrix, key, item)
    if classtype == 'Matrix':
        returnMatrix = Matrix(nrow=nrow, ncol=ncol, data=data)
        for key, item in object.items():
            setattr(returnMatrix.matrix, key, item)
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
        for _items in row:
            data.append()
    return data


def CSVExport(MatrixObject):
    data = MatrixObject.matrix.data
    nrow = MatrixObject.matrix.nrow
    ncol = MatrixObject.matrix.ncol
    CSVEncoder(data, nrow, ncol)


def CSVEncoder(data, nrow, ncol):
    pass


try:
    import tkinter
    from tkinter import messagebox
    from tkinter import filedialog

    def fileChooserUI():
        main = tkinter.Tk()
        main.withdraw()
        main.sourceFolder = ''
        main.sourceFile = ''
        main.sourceFile = filedialog.askopenfilename(
            parent=main, initialdir="/", title='Please select a directory')
        main.destroy()
        main.mainloop()
        return main.sourceFile

    def folderChooserUI():
        main = tkinter.Tk()
        main.withdraw()
        main.sourceFolder = ''
        main.sourceFile = ''
        main.sourceFolder = filedialog.askdirectory(
            parent=main, initialdir="/", title='Please select a directory')
        main.destroy()
        main.mainloop()
        return main.sourceFolder
except ImportError as e:
    """Tkinter or Tk or Tk bindings not installed \n
        enter the file path by text\n
        or install tkinter"""
    print("Tkinter or Tk or Tk bindings not installed \n \
          enter the file path by text\n \
          or install tkinter")
