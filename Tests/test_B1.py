import pytest
from pyrix import BinaryMatrix
from pyrix.exception import *
import copy

data = [
    [[0, 1], [1, 0]],
    [[0, 1, 1], [0, 0, 0], [1, 0, 1]],
    [[0, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 0], [1, 1, 0, 0]],
    [
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ],
]


@pytest.fixture(scope="session")
def test_BinMatrixinit():
    (rows, cols) = [2, 3, 4, 5], [2, 3, 4, 5]
    objects = []
    traversal = 0
    try:
        for (r, c, d) in zip(rows, cols, data):
            objects.append(BinaryMatrix(nrow=r, ncol=c, data=d, mode="EBM"))
            traversal += 1
    except incompaitableTypeException:
        print("Incompaitable Sizes")
    return objects


def test_BinMatrix_data(test_BinMatrixinit):
    cases = 4
    (rows, cols) = [2, 3, 4, 5], [2, 3, 4, 5]
    traversal = 0
    for (r, c, d) in zip(rows, cols, data):
        assert (
            test_BinMatrixinit[traversal].matrix.classType == "BinaryMatrix"
        ), "Matrix Object Creation Failed"
        assert test_BinMatrixinit[traversal].matrix.dimensions == [
            r,
            c,
        ], "nrows,ncols fail to match"
        assert (
            test_BinMatrixinit[traversal].matrix.data == d
        ), "Data initialization failed"
        traversal += 1
    print("Ran Initialization Test on", cases, " test cases")


def test_BinMatrix_is_square(test_BinMatrixinit):
    for i in range(len(test_BinMatrixinit)):
        assert (
            test_BinMatrixinit[i].isSquareMatrix() == True
        ), "Square Matrix Declared wrongly"
    print("Square Matrices correctly recognized")


def test_BinMatrix_is_binary(test_BinMatrixinit):
    for i in range(len(test_BinMatrixinit)):
        assert (
            test_BinMatrixinit[i].isBinaryMatrix() == True
        ), "Square Matrix Declared wrongly"
    print("Binary Matrices correctly recognized")


def test_BinMatrix_equals(test_BinMatrixinit):
    copylist = copy.deepcopy(test_BinMatrixinit)
    for i in range(len(test_BinMatrixinit)):
        assert test_BinMatrixinit[i].equals(copylist[i]), "Equals function test"
        assert test_BinMatrixinit[i] == copylist[i], "Equals Operator not working"
    print("Equal() method working correctly")


def test_BinMatrix_copy(test_BinMatrixinit):
    copylist = test_BinMatrixinit.copy()
    assert test_BinMatrixinit == copylist, "Copy method works properly"
    print("Copy() method working correctly")
