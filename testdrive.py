import sys
import Matrix as M
import binMat as B
d = [[2, 3, 9], [2, 11, 5]]
st = [[2, 4, 2], [2, 1, 1], [2, 1, 4]]
nrow = 2
ncol = 3
da = [[1, 1], [0, 1]]
dd = [[1, 1], [1, 1]]
ads = B.BinaryMatrix(nrow=2, ncol=2, data=da)
b = B.BinaryMatrix(nrow=2, ncol=2, data=dd)
z = M.Matrix(nrow=nrow, ncol=ncol, data=d)
r = M.Matrix(nrow=3, ncol=3, data=st)
try:
    print(r)
    print(b)
    print(b.isSquareMatrix())
    sdsa = b*ads
    print(sdsa)
    f = r.RrowEchleonTransform()
    s = ads.matrixRank()
    r.subRows(1, f, 1)
    f.RoundOff(2)
    mat = M.randomMatrix(scale="large", type="int")
    print(mat)
except M.incompaitableTypeException as e:
    print(e)
except M.nonInvertibleException as e:
    print(e)
except M.bitWiseOnMatrix as e:
    print(e)
