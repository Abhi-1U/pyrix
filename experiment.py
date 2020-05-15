
def strassenMultiplication(matrixdata1, matrixdata2, dims1, dims2):
    """follows strassens algorithm for matrix multiplication and does operations on larger
    nxn matrices where n is even.\n
    Returns a Matrix object
    """
    if(dims1[0] != dims1[1] and dims2[1] != dims2[0]):
        pass
    if(dims1[0] % 2 == 1):
        pass
    else:
        if dims1[0] == 2:
            return strassen2x2(matrixdata1, matrixdata2)
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
                combinedmat = combinematrices(returnmatrix)
                return combinedmat


def partitionmatrix(data, dims):
    """Partitions The given matrix into 4 quadrants\n
    Quadrant2  | Quadrant 1 \n
    ____________________
    Quadrant3  | Quadrant4\n
    \n
    This allows for Divide and Conquer Algorithms to function.\n
    Helper method in strassens Multiplication.\n
    Returns a list of 4 Quadrant nested lists.
    """
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
                quadrant3.append(data[i][j])
            if(minrows <= i < newnrows) and (newncols <= j < maxcols):
                quadrant1.append(data[i][j])
            if(newnrows <= i < maxrows) and (newncols <= j < maxcols):
                quadrant4.append(data[i][j])
    return [unlistifydata(quadrant2, newnrows, newncols), unlistifydata(quadrant1, newnrows, newncols), unlistifydata(quadrant3, newnrows, newncols), unlistifydata(quadrant4, newnrows, newncols)]


def unlistifydata(data, rowcount, colcount):
    """converts a single listed matrix into nested listed matrix.
    """
    clist = data
    nested = []
    for i in range(rowcount):
        nested.append(clist[0:colcount])
        del clist[0:colcount]
    return nested


def strassenNxN(listedminimatrixm1, listedminimatrixm2):
    t1 = listedminimatrixm1
    t2 = listedminimatrixm2
    M1 = (t1[0][0]+t1[1][1])*(t2[0][0]+t2[1][1])
    M2 = (t1[1][0]+t1[1][1])*t2[0][0]
    M3 = t1[0][0]*(t2[0][1]-t2[1][1])
    M4 = t2[1][1]*(t2[1][0]-t2[0][0])
    M5 = (t1[0][0]+t1[0][1])*t2[1][1]
    M6 = (t1[1][0]-t1[0][0])*(t2[0][0]+t2[0][1])
    M7 = (t1[0][1]-t1[1][1])*(t2[1][0]+t2[1][1])
    mtx = [[M1+M4-M5+M7, M3+M5], [M2+M4, M1-M2+M3+M6]]
    return mtx


def strassen2x2(m1, m2):
    """strassen multiplication module for 2 (2x2) matrices.\n
        Returns a nested list of matrix data.
    """
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


def combinematrices(nestedmatrix):
    quadrant2 = nestedmatrix[0]
    quadrant1 = nestedmatrix[1]
    quadrant3 = nestedmatrix[2]
    quadrant4 = nestedmatrix[3]
    combinedlistedmatrix1 = []
    combinedlistedmatrix2 = []
    for q2, q1, q3, q4 in zip(quadrant2, quadrant1, quadrant3, quadrant4):
        combinedlistedmatrix1.append(q2+q1)
        combinedlistedmatrix2.append(q3+q4)
    return combinedlistedmatrix1+combinedlistedmatrix2


def scaleMatrix(data, scalar):
    """Scales the Value of the data in the matrix object by the scalar value\n
        Returns NoneType and should not be assigned to a variable
    """
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] *= scalar
    return data


m1 = [[1, 2], [3, 4]]
m2 = [[1, 2], [3, 4]]
m3 = [[1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [
    1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4, 3, 4]]
m4 = [[2, 2, 1, 1], [2, 2, 1, 1], [3, 3, 4, 4], [3, 3, 4, 4]]
m5 = [[2, 2, 1, 1], [2, 2, 1, 1], [3, 3, 4, 4], [3, 3, 4, 4]]
print(combinematrices(partitionmatrix(m4, [4, 4])))
print(strassenMultiplication(m4, m5, [4, 4], [4, 4]))
print(strassen2x2(m1, m2))
