import pytest
from pyrix import Matrix, unitMatrix, zeroMatrix, randomMatrix, identityMatrix
from pyrix.exception import incompaitableTypeException, divisionErrorException, bitWiseOnMatrix
import copy
from pyrix.util import flipDimensions,Copy,JSONExport,JSONImport,nestifyMatrix,listifyMatrix
import math
data = [
    [
        [2.5, 3.3],
        [6.3, 0]
    ],
    [
        [1.1134, 23.2165, 90.4564],
        [2.4453, 23.2351, 91.8869],
        [1.0011, 56.4221, 0.54322]
    ],
    [
        [4.935264587402344e-05, 2.765655517578125e-05,
            2.86102294921875e-05, 3.0517578125e-05],
        [3.4809112548828125e-05, 3.814697265625e-05,
            4.172325134277344e-05, 0.00010323524475097656],
        [7.915496826171875e-05, 8.416175842285156e-05,
            8.96453857421875e-05, 9.703636169433594e-05],
        [0.00010395050048828125, 0.00011372566223144531,
            0.00011777877807617188, 0.00012445449829101562]
    ],
    [
        [0.2511575222015381, 0.2516036033630371, 0.2521524429321289,
            0.2523155212402344, 0.25193333625793457],
        [0.2519676685333252, 0.2544589042663574, 0.25499844551086426,
            0.2547335624694824, 0.25522279739379883],
        [0.2551295757293701, 0.2559933662414551, 0.256514310836792,
            0.25737428665161133, 0.2577781677246094],
        [0.2581827640533447, 0.2585480213165283, 0.25943970680236816,
            0.2707202434539795, 0.26087403297424316],
        [0.26274585723876953, 0.263012170791626, 0.2636113166809082,
            0.26253175735473633, 0.2637825012207031]
    ]
]
listed=[
    [2.5, 3.3,6.3, 0],
    [1.1134, 23.2165, 90.4564,2.4453, 23.2351, 91.8869,1.0011, 56.4221, 0.54322],
    [4.935264587402344e-05, 2.765655517578125e-05,
     2.86102294921875e-05, 3.0517578125e-05,3.4809112548828125e-05, 3.814697265625e-05,
     4.172325134277344e-05, 0.00010323524475097656,7.915496826171875e-05, 8.416175842285156e-05,
     8.96453857421875e-05, 9.703636169433594e-05,0.00010395050048828125, 0.00011372566223144531,
     0.00011777877807617188, 0.00012445449829101562],
    [0.2511575222015381, 0.2516036033630371, 0.2521524429321289,
     0.2523155212402344, 0.25193333625793457,0.2519676685333252, 0.2544589042663574, 0.25499844551086426,
     0.2547335624694824, 0.25522279739379883,0.2551295757293701, 0.2559933662414551, 0.256514310836792,
     0.25737428665161133, 0.2577781677246094,0.2581827640533447, 0.2585480213165283, 0.25943970680236816,
     0.2707202434539795, 0.26087403297424316,0.26274585723876953, 0.263012170791626, 0.2636113166809082,
     0.26253175735473633, 0.2637825012207031]
]

@pytest.fixture(scope="session")
def test_Matrixinit5():
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

def test_listifynestify(test_Matrixinit5):
    listings=[]
    copmat=Copy(test_Matrixinit5)
    for i in range(len(test_Matrixinit5)):
        listings.append(listifyMatrix(test_Matrixinit5[i]))
        assert listings[i]==listed[i]
    for i in range(len(test_Matrixinit5)):
        assert nestifyMatrix(listings[i],i+2,i+2)==data[i]
    

def test_JSON(test_Matrixinit5):
    for i in range(len(test_Matrixinit5)):
        JSONExport(test_Matrixinit5[i],"test.json")
        temp=JSONImport("test.json",mode="manual")
        assert temp==test_Matrixinit5[i]

def test_flipdims(test_Matrixinit5):
    for i in range(len(test_Matrixinit5)):
        assert flipDimensions(test_Matrixinit5[i])==test_Matrixinit5[i]