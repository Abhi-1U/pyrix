import pytest
from pyrix import Matrix,unitMatrix,zeroMatrix,randomMatrix,identityMatrix,Copy
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
adjointdata=[
    [
        [2, -2],
        [-2, 2]
    ],
    [
        [1, -2, 1],
        [11, -12, 3],
        [-15, 18, -5]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]

    ],
    [
        [0, 72, 0, 0, -72],
        [0, -84, 0, 0, 84],
        [0, -6, 0, 0, 6],
        [0, -24, 0, 0, 24],
        [0, 42, 0, 0, -42]

    ]
]
rankdata=[1,3,2,4]
symmetricdata = [True, False, False, False]
globalmeandata = [2, 4.888888889,4.5,3.48]
localrowmeandata = [2, 3.333333333,2.5,3]
localcolmeandata=[2,5.666666667,4.5,3.2]
globalmediandata=[2]
globalmodedata=[2,5,4,4]
localrowmodedata=[2,3,4,5]
localcolmodedata=[2,3,4,1]
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
    for i in range(len(test_Matrixinit)-1):
        assert test_Matrixinit[i].matrixRank()==rankdata[i]

def test_globalmean(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert round(test_Matrixinit[i].globalMean(),3) == round(globalmeandata[i],3)
def test_localrowmean(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert round(test_Matrixinit[i].localRowMean(0),3) == round(localrowmeandata[i], 3)


def test_localcolumnmean(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert round(test_Matrixinit[i].localColumnMean(0), 3) == round(localcolmeandata[i], 3)

def test_globalmode(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert test_Matrixinit[i].globalMode()==globalmodedata[i]

def test_localrowmode(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert test_Matrixinit[i].localRowMode(0)==localrowmodedata[i]
def test_localcolmode(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert test_Matrixinit[i].localColumnMode(0)==localcolmodedata[i]

def test_scale(test_Matrixinit):
    copymat=Copy(test_Matrixinit)
    for i in range(len(test_Matrixinit)):
        copymat[i].scaleMatrix(i+1)
    for i in range(len(test_Matrixinit)):
        copymat[i].scaleMatrix(1/(i+1))
        assert copymat[i]==test_Matrixinit[i]

def test_adjoint(test_Matrixinit):
    for i in range(len(test_Matrixinit)):
        assert test_Matrixinit[i].adjointTransform().matrix.data == adjointdata[i]
