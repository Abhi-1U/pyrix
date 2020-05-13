import sys
import Matrix as M
import binMat as B
d = [[2, 3, 9], [2, 11, 5]]
st = [[2, 4, 2], [2, 1, 1], [2, 1, 4]]
nrow = 2
ncol = 3
ls = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
da = [[1, 1], [1, 1]]
dd = [[1, 1], [1, 1]]
b = B.BinaryMatrix(nrow=2, ncol=2, data=dd)
z = M.Matrix(nrow=nrow, ncol=ncol, data=d)
r = M.Matrix(nrow=3, ncol=3, data=st)
ss = B.BinaryMatrix(nrow=2, ncol=2, data=da)
try:
    print(ss.partitionmatrix(data=ls, nrow=4, ncol=4))
except M.incompaitableTypeException as e:
    print(e)
except M.nonInvertibleException as e:
    print(e)
except M.bitWiseOnMatrix as e:
    print(e)
