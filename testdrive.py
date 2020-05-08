import sys
import Matrix as M
import binMat as B
d = [[2, 3, 9], [2, 11, 5]]
st = [[2, 4, 2], [2, 1, 1], [2, 1, 4]]
nrow = 2
ncol = 3
da = [[1, 4], [3, 2]]
dd = [[1, 1], [1, 1]]
b = B.BinaryMatrix(nrow=2, ncol=2, data=dd)
z = M.Matrix(nrow=nrow, ncol=ncol, data=d)
r = M.Matrix(nrow=3, ncol=3, data=st)
ss = M.Matrix(nrow=2, ncol=2, data=da)
try:
    print(r)
    print(b)

    l = ss.getAllMinors()
    print(l)
except M.incompaitableTypeException as e:
    print(e)
except M.nonInvertibleException as e:
    print(e)
except M.bitWiseOnMatrix as e:
    print(e)
