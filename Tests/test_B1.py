import pytest
from pyrix import BinaryMatrix,unitBinaryMatrix,zeroBinaryMatrix,randomBinaryMatrix,identityBinaryMatrix
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


def test_unitBmatrix():
    list = []
    for i in range(1,5):
        z=unitBinaryMatrix(nrow=i,ncol=i)
        list.append(z)
    for i in range(1,5):
        assert list[i-1].matrix.nrow == i
        assert list[i-1].matrix.ncol == i
        assert list[i-1].matrix.data[i-1][i-1] == 1


def test_zeroBmatrix():
    list = []
    for i in range(1,5):
        z=zeroBinaryMatrix(nrow=i,ncol=i)
        list.append(z)
    for i in range(1,5):
        assert list[i-1].matrix.nrow == i
        assert list[i-1].matrix.ncol == i
        assert list[i-1].matrix.data[i-1][i-1] == 0


def test_randomBmatrix():
    list = []
    for i in range(1,5):
        list.append(randomBinaryMatrix(scale="small", type="int"))
        list.append(randomBinaryMatrix(scale="small", type="float"))
        list.append(randomBinaryMatrix(scale="large", type="int"))
        list.append(randomBinaryMatrix(scale="large", type="float"))
    for i in range(0,4):
        pass

def test_IdentityBMatrix():
    list = []
    for i in range(1, 5):
        z = identityBinaryMatrix(nrow=i, ncol=i)
        list.append(z)
    for i in range(1, 5):
        assert list[i-1].matrix.nrow == i
        assert list[i-1].matrix.ncol == i
        assert list[i-1].matrix.data[i-1][i-1] == 1
        if(i>1):
            assert list[i-1].matrix.data[i-1][0]==0


def test_transpose(test_BinMatrixinit):
    transposes = []
    for i in range(len(test_BinMatrixinit)):
        transposes.append(test_BinMatrixinit[i].transposeTransform())
    for i in range(len(test_BinMatrixinit)):
        assert transposes[i].transposeTransform().matrix.data == test_BinMatrixinit[i].matrix.data


def test_getrow(test_BinMatrixinit):
    rows = []
    for i in range(len(test_BinMatrixinit)):
        rows.append(test_BinMatrixinit[i].getRow(i))
    for i in range(len(test_BinMatrixinit)):
        assert rows[i].matrix.data[0] == test_BinMatrixinit[i].matrix.data[i]
        print(test_BinMatrixinit[i])
