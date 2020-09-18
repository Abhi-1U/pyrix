import pytest
from pyrix import Vector,unitVector,zeroVector,randomVector,linearVector
from pyrix.exception import incompaitableTypeException

data = [[1], [1, 3], [2, 3, 4], [5, 4, 3, 5]]


@pytest.fixture(scope="session")
def test_Vectorinit():
    dims = [1, 2, 3, 4, 5]
    objects = []
    traversal = 0
    try:
        for (dim, d) in zip(dims, data):
            objects.append(Vector(dims=dim, data=d))
            traversal += 1
    except incompaitableTypeException:
        print("Incompaitable Sizes")
    return objects


def test_vector_data(test_Vectorinit):
    cases = 4
    dims = [1, 2, 3, 4]
    traversal = 0
    for (dim, d) in zip(dims, data):
        assert (
            test_Vectorinit[traversal].vector.classType == "Vector"
        ), "Vector Object Creation Failed"
        assert (
            test_Vectorinit[traversal].vector.dimensions == dim
        ), "dimensions fail to match"
        assert test_Vectorinit[traversal].vector.data == d, "Data initialization failed"
        traversal += 1
    print("Ran Initialization Test on", cases, " test cases")


def test_unitVector():
    list = []
    for i in range(1, 5):
        z = unitVector(dims=i)
        list.append(z)
    for i in range(1, 5):
        assert list[i-1].vector.dimensions == i
        assert list[i-1].vector.data[i-1] == 1


def test_zeroVector():
    list = []
    for i in range(1, 5):
        z = zeroVector(dims=i)
        list.append(z)
    for i in range(1, 5):
        assert list[i-1].vector.dimensions == i
        assert list[i-1].vector.data[i-1] == 0


def test_randomVector():
    list = []
    for i in range(1, 5):
        list.append(randomVector(scale="large", type="int"))
    for i in range(0, 4):
        pass


def test_linearVector():
    list = []
    for i in range(2, 5):
        z = linearVector(dims=i,minVal=0,maxVal=6)
        list.append(z)
    for i in range(2, 5):
        assert list[i-2].vector.dimensions == i
