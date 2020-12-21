#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix/Utilities\n
Author      : Abhi-1U <https://github.com/Abhi-1U>\n
Description : Utility Extention to pyrix  \n
Encoding    : UTF-8\n
Version     :0.7.19\n
Build       :0.7.19/21-12-2020
"""

# *------- Imports ------------------------------------------------------------*

from pyrix.matrix import Matrix
from pyrix.binarymatrix import BinaryMatrix
from pyrix.vector import Vector
from pyrix.exception import binaryMatrixException, incompaitableTypeException
import json
import copy

#*-----------------------------------------------------------------------------*

#*------- pyrix.util.reDimensionalize() ---------------------------------------*

def reDimensionalize(AnyMatrixObject, nrow, ncol):
    """
    This function redimensionalizes the given matrix object to the new row and 
    column parameters.
    """
    listifieddata = listifyMatrix(AnyMatrixObject)
    matrixdata = []
    for i in range(nrow):
        matrixdata.append([])
        matrixdata[i] = listifieddata[0:ncol]
        del listifieddata[0:ncol]
    if AnyMatrixObject.matrix.classType == "Matrix":
        return Matrix(nrow=nrow, ncol=ncol, data=matrixdata)
    if AnyMatrixObject.matrix.classType == "BinaryMatrix":
        return BinaryMatrix(nrow=nrow, ncol=ncol, data=matrixdata)
    if isinstance(AnyMatrixObject, Vector):
        print("reDimensionalize not applicable on Vectors")

#*------- pyrix.util.listifyMatrix() ---------------------------------------*

def listifyMatrix(MatrixObject):
    """
    This function returns a single list of all values in the matrix object's
    nested list structure.
    """
    matrixdata = MatrixObject.matrix.data
    listifiedmatrix = []
    for i in range(MatrixObject.matrix.nrow):
        for j in range(MatrixObject.matrix.ncol):
            listifiedmatrix.append(matrixdata[i][j])
    MatrixObject.matrix.listifieddata = listifiedmatrix
    return listifiedmatrix

#*------- pyrix.util.nestifyMatrix() ---------------------------------------*

def nestifyMatrix(listeddata, rowcount, colcount):
    """
    Performs the inverse function of listifymatrix() method. 
    """
    clist = listeddata
    nested = []
    for _i in range(rowcount):
        nested.append(clist[0:colcount])
        del clist[0:colcount]
    return nested

#*------- pyrix.util.flipDimensions() ---------------------------------------*

def flipDimensions(AnyMatrixObject):
    """
    Flips the row and column parameters and redimensionalizes the matrix. 
    """
    newcol = AnyMatrixObject.matrix.nrow
    newrow = AnyMatrixObject.matrix.ncol
    return reDimensionalize(AnyMatrixObject, newrow, newcol)

#*------- pyrix.util.Copy() ---------------------------------------*

def Copy(AnyObject):
    """
    returns a deep copy of the matrix object.
    """
    return copy.deepcopy(AnyObject)

#*------- pyrix.util.JSONEncoder() ---------------------------------------*

def JSONEncoder(object):
    """
    Encodes dictionary data of the Matrix Object into JSON format.
    """
    Object = object
    return Object.matrix.__dict__

#*------- pyrix.util.JSONExport() ---------------------------------------*

def JSONExport(Object, filename):
    """
    Exports the Object data as an JSON file to save th eobject permanantely.
    """
    data = JSONEncoder(Object)
    with open(filename, "w") as outfile:
        json.dump(data, outfile)
        outfile.close()
    print("Export Of Object Data Successfull!")

#*------- pyrix.util.JSONDecoder() ---------------------------------------*

def JSONDecoder(object):
    """
    Decodes JSON File type\n
    returns a Matrix Object.
    """
    classtype = None
    nrow = 0
    ncol = 0
    data = []
    for key, item in object.items():
        if key == "classType":
            classtype = item
            continue
        if key == "nrow":
            nrow = item
            continue
        if key == "ncol":
            ncol = item
            continue
        if key == "data":
            data = item
            break
    if classtype == "BinaryMatrix":
        returnMatrix = BinaryMatrix(nrow=nrow, ncol=ncol, data=data)
        for key, item in object.items():
            setattr(returnMatrix.matrix, key, item)
    if classtype == "Matrix":
        returnMatrix = Matrix(nrow=nrow, ncol=ncol, data=data)
        for key, item in object.items():
            setattr(returnMatrix.matrix, key, item)
    return returnMatrix

#*------- pyrix.util.JSONImport() ---------------------------------------*

def JSONImport(filename, mode="UI"):
    """
    Allows for JSON files to be read and recreate the objects\n
    If you have Tkinter installed then the UI mode will trigger the GUI to
    select file. Returns a Matrix Object.
    """
    if mode == "UI":
        filepath = fileChooserUI()
    else:
        filepath = filename
    with open(filepath, "r") as openfile:
        json_object = json.load(openfile)
        openfile.close()
    return JSONDecoder(json_object)


try:
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import Tk

    def fileChooserUI():
        main = Tk()
        main.withdraw()
        main.sourceFolder = ""
        main.sourceFile = ""
        main.sourceFile = filedialog.askopenfilename(
            parent=main, initialdir="/", title="Please select a directory"
        )
        main.destroy()
        main.mainloop()
        return main.sourceFile

    def folderChooserUI():
        main = Tk()
        main.withdraw()
        main.sourceFolder = ""
        main.sourceFile = ""
        main.sourceFolder = filedialog.askdirectory(
            parent=main, initialdir="/", title="Please select a directory"
        )
        main.destroy()
        main.mainloop()
        return main.sourceFolder


except ImportError as e:
    """
    [Warning] Tkinter or Tk or Tk bindings not installed \n
              enter the file path by text\n
              or install tkinter
    """
    print(
        "[Warning] Tkinter or Tk or Tk bindings not installed \n \
         enter the file path by text\n \
         or install tkinter"\
    )
