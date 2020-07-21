#!/usr/bin/python3
# -*- coding : UTF-8 -*-
"""
Name        : Pyrix\n
Author      : Abhi-1U <https://github.com/Abhi-1U> \n
Description : A Matrix manipulation library  \n
Encoding    : UTF-8\n
Version     : 0.6.14\n
Build       : 0.6.14/17-07-2020
"""

from pyrix.exception import(
    binaryMatrixException,
    bitWiseOnMatrix,
    divisionErrorException,
    incompaitableTypeException,
    nonInvertibleException)

from pyrix.matrix import (
    Matrix,
    zeroMatrix,
    unitMatrix,
    randomMatrix,
    identityMatrix
)
from pyrix.binarymatrix import (
    BinaryMatrix,
    identityBinaryMatrix,
    randomBinaryMatrix,
    unitBinaryMatrix,
    zeroBinaryMatrix
)
from pyrix.vector import (
    linearVector,
    randomVector,
    unitVector,
    Vector,
    zeroVector
)

from pyrix.util import (
    flipDimensions,
    JSONImport,
    reDimensionalize,
    nestifyMatrix,
    JSONExport,
    Copy
)