import pytest
from pyrix import Matrix,unitMatrix,zeroMatrix,randomMatrix,identityMatrix
from pyrix.exception import incompaitableTypeException,divisionErrorException,bitWiseOnMatrix
import copy

# Test Suite M1
# Square matrices are test
data = [
    [
        [2, 2], 
        [2, 2]
    ],
    [   
        [3, 4, 3], 
        [5, 5, 4], 
        [9, 6, 5]
    ],
    [
        [4, 3, 2, 1], 
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [8, 7, 6, 5]
    ],
    [
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 1, 4, 5],
        [7, 6, 4, 6, 4],
        [1, 2, 3, 4, 5],
    ],
]
rankdata=[1,3,2,4]
symmetricdata = [True, False, False, False]

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

def test_unitmatrix():
    list=[]
    for i in range(1,5):
        list.append(unitMatrix(nrow=i,ncol=i))
    for i in range(1,5):
        assert list[i-1].matrix.nrow==i
        assert list[i-1].matrix.ncol==i
        assert list[i-1].matrix.data[i-1][i-1]==1


def test_zeromatrix():
    list = []
    for i in range(1,5):
        list.append(zeroMatrix(nrow=i, ncol=i))
    for i in range(1,5):
        assert list[i-1].matrix.nrow == i
        assert list[i-1].matrix.ncol == i
        assert list[i-1].matrix.data[i-1][i-1] == 0


def test_randommatrix():
    list = []
    for i in range(1,5):
        list.append(randomMatrix(scale="small",type="int"))
        list.append(randomMatrix(scale="large",type="float"))
        list.append(randomMatrix(scale="small",type="float"))
        list.append(randomMatrix(scale="large",type="int"))
    for i in range(0,4):
        pass


def test_IdentityMatrix():
    list = []
    for i in range(1, 5):
        z = identityMatrix(nrow=i, ncol=i)
        list.append(z)
    for i in range(1, 5):
        assert list[i-1].matrix.nrow == i
        assert list[i-1].matrix.ncol == i
        assert list[i-1].matrix.data[i-1][i-1] == 1
        if(i > 1):
            assert list[i-1].matrix.data[i-1][0] == 0


def test_transposeMatrix(test_Matrixinit):
    transposes = []
    for i in range(len(test_Matrixinit)):
        transposes.append(test_Matrixinit[i].transposeTransform())
    for i in range(len(test_Matrixinit)):
        assert transposes[i].transposeTransform().matrix.data == test_Matrixinit[i].matrix.data


def test_getrow(test_Matrixinit):
    rows = []
    for i in range(len(test_Matrixinit)):
        rows.append(test_Matrixinit[i].getRow(i))
    for i in range(len(test_Matrixinit)):
        assert rows[i].matrix.data[0] == test_Matrixinit[i].matrix.data[i]

def test_truedivision(test_Matrixinit):
    dummy=Matrix(nrow=1,ncol=1,data=[[1]])
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i]/dummy
    except divisionErrorException as e:
        pass


def test_floordivision(test_Matrixinit):
    dummy = Matrix(nrow=1, ncol=1, data=[[1]])
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i]//dummy
    except divisionErrorException as e:
        pass

def test_modulus(test_Matrixinit):
    dummy=Matrix(nrow=1,ncol=1,data=[[1]])
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i]%dummy
    except divisionErrorException as e:
        pass


def test_lshift(test_Matrixinit):
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i]<<2
    except bitWiseOnMatrix as e:
        pass


def test_rshift(test_Matrixinit):
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i]>>2
    except bitWiseOnMatrix as e:
        pass

def test_and(test_Matrixinit):
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i]&2
    except bitWiseOnMatrix as e:
        pass

def test_or(test_Matrixinit):
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i]|2
    except bitWiseOnMatrix as e:
        pass


def test_xor(test_Matrixinit):
    try:
        for i in range(len(test_Matrixinit)):
            test_Matrixinit[i] ^ 2
    except bitWiseOnMatrix as e:
        pass

def test_invert(test_Matrixinit):
    try:
        for i in range(len(test_Matrixinit)):
            ~test_Matrixinit[i]
    except bitWiseOnMatrix as e:
        pass
def test_issymmetric(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert test_Matrixinit[i].isSymmetricMatrix()==symmetricdata[i]

def test_rank(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        try:
            assert test_Matrixinit[i].matrixRank()==rankdata[i]
        except ZeroDivisionError as e:
            print(test_Matrixinit[i])