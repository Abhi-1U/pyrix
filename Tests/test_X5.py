import pytest
from pyrix.exception import (
    binaryMatrixException,
    bitWiseOnMatrix,
    divisionErrorException,
    incompaitableTypeException,
    nonInvertibleException,
)
from pyrix import Matrix, BinaryMatrix

data = [
    [[1, 1], [2, 2]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[4, 3, 2, 1], [1, 2, 3, 4]],
    [
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 1, 4, 5],
        [7, 6, 4, 6, 4],
        [0, 0, 0, 0, 0],
    ],
]


@pytest.fixture(scope="session")
def test_XMatrixinit():
    (rows, cols) = [2, 3, 4, 5], [2, 3, 4, 5]
    objects = []
    traversal = 0
    for (r, c, d) in zip(rows, cols, data):
        if r == 2:
            try:
                objects.append(BinaryMatrix(nrow=r, ncol=c, data=d, mode="EBM"))
            except binaryMatrixException as e:
                print(e, "\n", "Test passed succesfully")
                objects.append(Matrix(nrow=r, ncol=c, data=d))
        if r == 4 and c == 4:
            try:
                objects.append(Matrix(nrow=r, ncol=c, data=d))
            except incompaitableTypeException:
                print("Incompaitable Sizes")
                objects.append(Matrix(nrow=2, ncol=c, data=d))
        else:
            objects.append(Matrix(nrow=r, ncol=c, data=d))
        traversal += 1
    return objects

def test_BitWiseException(test_XMatrixinit):
    for i in range(len(test_XMatrixinit)):
        try:
            test_XMatrixinit[i] << 3
        except bitWiseOnMatrix as e:
            print(e, "\n Test Succesfull")


def test_DivisionException(test_XMatrixinit):
    for i in range(len(test_XMatrixinit)):
        try:
            test_XMatrixinit[i] / test_XMatrixinit[i]
        except divisionErrorException as e:
            print(e, "\n Test Succesfull")

def test_NotInvertibleException(test_XMatrixinit):
    try:
        test_XMatrixinit[2].invertMatrix()
    except nonInvertibleException as e:
        print(e, "\n Test Succesfull")
