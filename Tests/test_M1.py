import pytest
from pyrix import Matrix
from pyrix.exception import incompaitableTypeException
import copy

# Test Suite M1
# Square matrices are test
data = [
    [[2, 2], [2, 2]],
    [[3, 4, 3], [5, 5, 4], [9, 6, 5]],
    [[4, 3, 2, 1], [1, 2, 3, 4], [5, 6, 7, 8], [8, 7, 6, 5]],
    [
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 1, 4, 5],
        [7, 6, 4, 6, 4],
        [0, 0, 0, 0, 0],
    ],
]


@pytest.fixture(scope="session")
def test_Matrixinit():
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


def test_Matrix_data(test_Matrixinit):
    cases = 4
    (rows, cols) = [2, 3, 4, 5], [2, 3, 4, 5]
    traversal = 0
    for (r, c, d) in zip(rows, cols, data):
        assert (
            test_Matrixinit[traversal].matrix.classType == "Matrix"
        ), "Matrix Object Creation Failed"
        assert test_Matrixinit[traversal].matrix.dimensions == [
            r,
            c,
        ], "nrows,ncols fail to match"
        assert test_Matrixinit[traversal].matrix.data == d, "Data initialization failed"
        traversal += 1
    print("Ran Initialization Test on", cases, " test cases")


def test_Matrix_isquare(test_Matrixinit):

    for i in range(len(test_Matrixinit)):
        assert (
            test_Matrixinit[i].isSquareMatrix() == True
        ), "Square Matrix Declared wrongly"
    print("Square Matrices correctly recognized")


def test_Matrix_equals(test_Matrixinit):
    copylist = copy.deepcopy(test_Matrixinit)
    for i in range(len(test_Matrixinit)):
        assert test_Matrixinit[i].equals(copylist[i]), "Equals function test"
        assert test_Matrixinit[i] == copylist[i], "Equals Operator not working"
    print("Equal() method working correctly")


def test_Matrix_copy(test_Matrixinit):
    copylist = test_Matrixinit.copy()
    assert test_Matrixinit == copylist, "Copy method works properly"
    print("Copy() method working correctly")
