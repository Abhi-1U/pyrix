import pytest
from pyrix import Vector,unitVector,zeroVector,randomVector,linearVector,Copy
from pyrix.exception import incompaitableTypeException,divisionErrorException,bitWiseOnMatrix

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
        print(test_Vectorinit[traversal])
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
        list.append(randomVector(scale="small", type="float"))
        list.append(randomVector(scale="small", type="int"))
        list.append(randomVector(scale="large", type="float"))
    for i in range(0, 4):
        pass


def test_linearVector():
    list = []
    for i in range(2, 5):
        z = linearVector(dims=i,minVal=0,maxVal=6)
        list.append(z)
    for i in range(2, 5):
        assert list[i-2].vector.dimensions == i


def test_truedivision(test_Vectorinit):
    dummy = Vector(dims=1, data=[1])
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i]/dummy
    except divisionErrorException as e:
        pass


def test_floordivision(test_Vectorinit):
    dummy = Vector(dims=1, data=[1])
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i]//dummy
    except divisionErrorException as e:
        pass


def test_modulus(test_Vectorinit):
    dummy = Vector(dims=1, data=[1])
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i]%dummy
    except divisionErrorException as e:
        pass


def test_lshift(test_Vectorinit):
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i] << 2
    except bitWiseOnMatrix as e:
        pass


def test_rshift(test_Vectorinit):
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i] >> 2
    except bitWiseOnMatrix as e:
        pass

def test_and(test_Vectorinit):
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i] & 2
    except bitWiseOnMatrix as e:
        pass


def test_or(test_Vectorinit):
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i] | 2
    except bitWiseOnMatrix as e:
        pass


def test_xor(test_Vectorinit):
    try:
        for i in range(len(test_Vectorinit)):
            test_Vectorinit[i] ^ 2
    except bitWiseOnMatrix as e:
        pass


def test_invert(test_Vectorinit):
    try:
        for i in range(len(test_Vectorinit)):
            ~test_Vectorinit[i]
    except bitWiseOnMatrix as e:
        pass




def test_add(test_Vectorinit):
    cVector=test_Vectorinit.copy()
    sums=[]
    for i in range(len(test_Vectorinit)):
        sums.append(cVector[i]+test_Vectorinit[i])
    for i in range(len(test_Vectorinit)):
        assert sums[i]==test_Vectorinit[i].scaleVector(2)

def test_sub(test_Vectorinit):
    cVector=test_Vectorinit.copy()
    sums=[]
    for i in range(len(test_Vectorinit)):
        sums.append(cVector[i]-test_Vectorinit[i])
    for i in range(len(test_Vectorinit)):
        assert sums[i]==test_Vectorinit[i].scaleVector(0)

  
