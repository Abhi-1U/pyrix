import pytest
from pyrix import Matrix, unitMatrix, zeroMatrix, randomMatrix, identityMatrix, Copy
from pyrix.exception import incompaitableTypeException, divisionErrorException, bitWiseOnMatrix
import copy

data=[
    [
        [1,2],
        [0,1]
    ],
    [
        [1,2,3],
        [0,1,2],
        [0,0,1]
    ],
    [
        [1,2,3,4],
        [0,1,2,3],
        [0,0,1,2],
        [0,0,0,1]
    ],
    [
        [1,0,0,0,0],
        [2,1,0,0,0],
        [3,2,1,0,0],
        [4,3,2,1,0],
        [5,4,3,2,1]
    ]
]
lowertriangularitydata=[True,True,True,False]
uppertriangularitydata=[False,False,False,True]
orthogonalmatrixdata = [False, False, False, False]
inversedata=[True,True,True,True]
@pytest.fixture(scope="session")
def test_Matrixinit2():
    (rows, cols) = [2, 3, 4, 5], [2, 3, 4, 5]
    objects = []
    traversal = 0
    try:
        for (r, c, d) in zip(rows, cols, data):
            objects.append(Matrix(nrow=r, ncol=c, data=d))
            traversal += 1
    except incompaitableTypeException:
        print("Incompaitable Sizes")
    return objects

def test_trace(test_Matrixinit2):
    for i in range(len(test_Matrixinit2)):
        assert test_Matrixinit2[i].matrixTrace()==i+2

def test_lowerTriangular(test_Matrixinit2):
    for i in range(len(test_Matrixinit2)):
        assert test_Matrixinit2[i].isLowerTriangularMatrix()==lowertriangularitydata[i]
def test_upperTriangularity(test_Matrixinit2):
    for i in range(len(test_Matrixinit2)):
        assert test_Matrixinit2[i].isUpperTriangularMatrix()==uppertriangularitydata[i]

def test_orthogonality(test_Matrixinit2):
    for i in range(len(test_Matrixinit2)):
        assert test_Matrixinit2[i].isOrthogonalMatrix()==orthogonalmatrixdata[i]

def test_invertibility(test_Matrixinit2):
    for i in range(len(test_Matrixinit2)):
        assert test_Matrixinit2[i].isInvertible()==inversedata[i]

