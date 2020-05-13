
def strassenMultiplication(matrixdata1, matrixdata2, dims1, dims2):
    if(dims1[0] != dims1[1] and dims2[1] != dims2[0]):
        pass
    else:
        if dims1[0] == 2:
            return strassen2x2(m1, m2)
        else:
            if(dims1[0] % 2 == 0):
                parts = 4
                newval = int(dims1[0]/(parts/2))
                returnmatrix = []
                p1 = partitionmatrix(matrixdata1, dims1)
                p2 = partitionmatrix(matrixdata2, dims2)
                print(p1)
                print(p2)
                for minimatrix1, minimatrix2 in zip(p1, p2):
                    returnmatrix.append(strassenMultiplication(
                        minimatrix1, minimatrix2, dims1=[newval, newval], dims2=[newval, newval]))

                scaleMatrix(returnmatrix, int(dims1[0]/2))
                return returnmatrix


def partitionmatrix(data, dims):
    parts = 4
    newnrows = int(dims[0]/(parts/2))
    newncols = int(dims[1]/(parts/2))
    maxrows = len(data)
    maxcols = len(data[0])
    minrows = 0
    mincols = 0
    quadrant1 = []
    quadrant2 = []
    quadrant3 = []
    quadrant4 = []
    for i in range(minrows, maxrows):
        for j in range(mincols, maxcols):
            if(minrows <= i < newnrows)and(mincols <= j < newncols):
                quadrant2.append(data[i][j])
            if(newnrows <= i < maxrows) and (mincols <= j < newncols):
                quadrant1.append(data[i][j])
            if(minrows <= i < newnrows) and (newncols <= j < maxcols):
                quadrant3.append(data[i][j])
            if(newnrows <= i < maxrows) and (newncols <= j < maxcols):
                quadrant4.append(data[i][j])
    return [unlistifydata(quadrant2, newnrows, newncols), unlistifydata(quadrant1, newnrows, newncols), unlistifydata(quadrant3, newnrows, newncols), unlistifydata(quadrant4, newnrows, newncols)]


def unlistifydata(data, rowcount, colcount):
    clist = data
    nested = []
    for i in range(rowcount):
        nested.append(clist[0:colcount])
        del clist[0:colcount]
    return nested


def strassen2x2(m1, m2):
    t1 = m1
    t2 = m2
    M1 = (t1[0][0]+t1[1][1])*(t2[0][0]+t2[1][1])
    M2 = (t1[1][0]+t1[1][1])*t2[0][0]
    M3 = t1[0][0]*(t2[0][1]-t2[1][1])
    M4 = t2[1][1]*(t2[1][0]-t2[0][0])
    M5 = (t1[0][0]+t1[0][1])*t2[1][1]
    M6 = (t1[1][0]-t1[0][0])*(t2[0][0]+t2[0][1])
    M7 = (t1[0][1]-t1[1][1])*(t2[1][0]+t2[1][1])
    mtx = [[M1+M4-M5+M7, M3+M5], [M2+M4, M1-M2+M3+M6]]
    return mtx


def scaleMatrix(data, scalar):
    """Scales the Value of the data in the matrix object by the scalar value\n
        Returns NoneType and should not be assigned to a variable
    """
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] *= scalar


m1 = [[1, 2], [3, 4]]
m2 = [[1, 2], [3, 4]]
m3 = [[1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [
    1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4]]

m4 = [[1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [
    1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4]]

print(strassen2x2(m1, m2))
print(strassenMultiplication(m3, m4, [8, 8], [8, 8]))
