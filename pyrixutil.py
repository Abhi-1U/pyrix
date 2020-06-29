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
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import Tk

    def fileChooserUI():
        main = Tk()
        main.withdraw()
        main.sourceFolder = ''
        main.sourceFile = ''
        main.sourceFile = filedialog.askopenfilename(
            parent=main, initialdir="/", title='Please select a directory')
        main.destroy()
        main.mainloop()
        return main.sourceFile

    def folderChooserUI():
        main = Tk()
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
