import sys
import Matrix as M
d = [[2, 3, 9], [2, 11, 5]]
st = [[2, 4, 2], [2, 1, 1], [2, 1, 4]]
nrow = 2
ncol = 3
z = M.Matrix(nrow=nrow, ncol=ncol, data=d)
r = M.Matrix(nrow=3, ncol=3, data=st)
try:
    print(r)
    f = r.RrowEchleonTransform()
    s = r.matrixRank()
    print(f)
    print(s)
except M.incompaitableTypeException as e:
    print(e)
except M.nonInvertibleException as e:
    print(e)
