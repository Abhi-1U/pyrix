import pytest
from pyrix import CharMatrix,alphaMatrix5x5
from pyrix.exception import incompaitableTypeException,divisionErrorException,bitWiseOnMatrix
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

coldata=[
    [
        ["a"],
        ["c"]
    ],
    [
        ["a"],
        ["d"],
        ["g"]
    ],
    [
        ["a"],
        ["d"],
        ["g"],
        ["m"]
    ],
    [
        ["a"],
        ["f"],
        ["l"],
        ["q"],
        ["v"]
    ]
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

def test_alpha5x5_alt():
    mat=alphaMatrix5x5(['h','e','l','l','o'])
    assert mat.matrix.data!=data[-1]

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

def test_ASCIIvals(test_CharMatrixinit):
    ASCIImatrix=[]
    for i in range(len(test_CharMatrixinit)):
        ASCIImatrix.append(test_CharMatrixinit[i].ASCIIvals())
    
    for i in range(len(test_CharMatrixinit)):
        for j in range(test_CharMatrixinit[i].matrix.nrow):
            for k in range(test_CharMatrixinit[i].matrix.ncol):
                assert chr(ASCIImatrix[i].matrix.data[j][k])==test_CharMatrixinit[i].matrix.data[j][k]
    
def test_findcharactar(test_CharMatrixinit):

    for i in range(len(test_CharMatrixinit)):
        char=test_CharMatrixinit[i].findCharactar("a")
        assert test_CharMatrixinit[i].matrix.data[char[0]][char[1]]=="a"
    
def test_transpose(test_CharMatrixinit):
    transposes=[]
    for i in range(len(test_CharMatrixinit)):
        transposes.append(test_CharMatrixinit[i].transposeTransform())
    for i in range(len(test_CharMatrixinit)):
        assert transposes[i].transposeTransform().matrix.data ==test_CharMatrixinit[i].matrix.data

def test_getrow(test_CharMatrixinit):
    rows=[]
    for i in range(len(test_CharMatrixinit)):
        rows.append(test_CharMatrixinit[i].getRow(i))
    for i in range(len(test_CharMatrixinit)):
        assert rows[i].matrix.data[0]==test_CharMatrixinit[i].matrix.data[i]


def test_truedivision(test_CharMatrixinit):
    dummy = CharMatrix(nrow=1, ncol=1, data=[["A"]])
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i]/dummy
    except divisionErrorException as e:
        pass


def test_floordivision(test_CharMatrixinit):
    dummy = CharMatrix(nrow=1, ncol=1, data=[["A"]])
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i]//dummy
    except divisionErrorException as e:
        pass


def test_modulus(test_CharMatrixinit):
    dummy = CharMatrix(nrow=1, ncol=1, data=[["A"]])
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i]%dummy
    except divisionErrorException as e:
        pass


def test_lshift(test_CharMatrixinit):
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i] << 2
    except bitWiseOnMatrix as e:
        pass


def test_rshift(test_CharMatrixinit):
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i] >> 2
    except bitWiseOnMatrix as e:
        pass


def test_and(test_CharMatrixinit):
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i] & 2
    except bitWiseOnMatrix as e:
        pass


def test_or(test_CharMatrixinit):
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i] | 2
    except bitWiseOnMatrix as e:
        pass


def test_xor(test_CharMatrixinit):
    try:
        for i in range(len(test_CharMatrixinit)):
            test_CharMatrixinit[i] ^ 2
    except bitWiseOnMatrix as e:
        pass


def test_invert(test_CharMatrixinit):
    try:
        for i in range(len(test_CharMatrixinit)):
            ~test_CharMatrixinit[i]
    except bitWiseOnMatrix as e:
        pass

def test_getcol(test_CharMatrixinit):
    for i in range(len(test_CharMatrixinit)):
        assert test_CharMatrixinit[i].getCol(0).matrix.data==coldata[i]
        print(test_CharMatrixinit[i])