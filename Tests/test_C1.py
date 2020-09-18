import pytest
from pyrix import CharMatrix,alphaMatrix5x5
from pyrix.exception import incompaitableTypeException
import copy

# Test Suite M1
# Square matrices are test
data = [
    [["a", "b"], ["c", "d"]],
    [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
    [
        ["a", "b", "c", "j"],
        ["d", "e", "f", "k"],
        ["g", "h", "i", "l"],
        ["m", "n", "o", "p"],
    ],
    [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "k"],
        ["l", "m", "n", "o", "p"],
        ["q", "r", "s", "t", "u"],
        ["v", "w", "x", "y", "z"],
    ],
]


@pytest.fixture(scope="session")
def test_CharMatrixinit():
    (rows, cols) = [2, 3, 4, 5], [2, 3, 4, 5]
    objects = []
    traversal = 0
    try:
        for (r, c, d) in zip(rows, cols, data):
            objects.append(CharMatrix(nrow=r, ncol=c, data=d))
            traversal += 1
    except incompaitableTypeException:
        print("Incompaitable Sizes")
    return objects


def test_CharMatrix_data(test_CharMatrixinit):
    cases = 4
    (rows, cols) = [2, 3, 4, 5], [2, 3, 4, 5]
    traversal = 0
    for (r, c, d) in zip(rows, cols, data):
        assert (
            test_CharMatrixinit[traversal].matrix.classType == "CharactarMatrix"
        ), "Matrix Object Creation Failed"
        assert test_CharMatrixinit[traversal].matrix.dimensions == [
            r,
            c,
        ], "nrows,ncols fail to match"
        assert (
            test_CharMatrixinit[traversal].matrix.data == d
        ), "Data initialization failed"
        traversal += 1
    print("Ran Initialization Test on", cases, " test cases")

def test_alpha5x5():
    mat=alphaMatrix5x5()
    assert mat.matrix.data==data[-1]


def test_CMatrix_copy(test_CharMatrixinit):
    copylist = test_CharMatrixinit.copy()
    assert test_CharMatrixinit == copylist, "Copy method works properly"
    print("Copy() method working correctly")


def test_Matrix_isquare(test_CharMatrixinit):

    for i in range(len(test_CharMatrixinit)):
        assert (
            test_CharMatrixinit[i].isSquareMatrix() == True
        ), "Square Matrix Declared wrongly"
    print("Square Matrices correctly recognized")
