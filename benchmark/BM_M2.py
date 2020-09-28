import time
import pyrix as px
import copy
import matplotlib.pyplot as pt
import numpy as np
from numpy.linalg import inv
benchdata = []
inputsize = list(range(1000))


def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        benchdata.append(runtime)
        return value
    return function_timer


@timerfunc
def pyrixbased(scale):
    mat = px.unitMatrix(nrow=scale, ncol=scale)
    mat.invertMatrix()


for i in inputsize:
    pyrixbased(i+1)
pyrixdata = copy.deepcopy(benchdata)
benchdata = []


@timerfunc
def numpybased(scale):
    mat = np.identity(scale, dtype=int)
    inv(mat)

for i in inputsize:
    numpybased(i+1)
numpydata = copy.deepcopy(benchdata)

ax = pt.subplot()
ax.plot(inputsize, pyrixdata, label="Pyrix")
ax.plot(inputsize, numpydata, label="Numpy")
pt.xlabel('Size of Matrix(nxn)')
# naming the y axis
pt.ylabel('Time taken in seconds(Lower is Better)')
# giving a title to my graph
pt.title('Object Creation Benchmark\nIntel J2900@2.41Ghz/Linux mint @ CPython3.6.9')
ax.legend()
pt.show()
