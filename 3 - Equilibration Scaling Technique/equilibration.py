import numpy as np

def Equilibration(array_A, array_c, array_b):
    
    print ("---------------Before Equilibration---------------\n")
    print("A = \n", array_A, "\n-----------")
    print("c = \n", array_c, "\n-----------")
    print("b = \n", array_b, "\n-----------")

    # Get number of rows/columns of array A
    numrows = len(array_A)
    numcols = len(array_A[0])

    colmax = []
    colmulti = []
    rowmulti = [0] * numrows
    colmax = np.array(colmax, dtype=float)
    colmulti = np.array(colmulti, dtype=float)
    rowmulti = np.array(rowmulti, dtype=float)

    # Max absolute value of each column
    max_column = 0

    # Row indices
    rows = []
    for i in range(numrows):
        rows.append(i)
    
    # Max by column
    max_column = np.amax(abs(array_A), axis=0)      # Get max value
    rows_max = np.argmax(abs(array_A), axis=0)      # Get row indice
    colmax = np.append(colmax, max_column)
    colmulti = np.append(colmulti, 1/max_column)
    rows_search = list(set(rows) - set(rows_max))   # Decide which rows are going to be parsed later on

    # Change array A: multiply every value in column i with 1/max_column
    for i in range(numcols):
        for j in range(numrows):
            temp1 = array_A[j, i] * colmulti[i]
            array_A[j, i] = temp1

    # Change array c: multiply every value in position i with 1/max_column
    for i in range(numrows):
        temp2 = array_c[i] * colmulti[i]
        array_c[i] = temp2

    # Compute rowmulti: for every row in rows_search, find absolute max_row and add 1/max_row to rowmulti
    #print(rows_search)
    for i in (rows_search):
        max_row = np.amax(abs(array_A[i, :]))
        rowmulti[i] = 1/max_row

    # Change array A: for every row in rows_search, multiply every value in that row with 1/max_row
    for i in range(numcols):
        for j in range(numrows):
            if (rowmulti[j] != 0):
                temp3 = array_A[i, j] * rowmulti[j]
                array_A[i, j] = temp3

    # Change array b: multiply every value in position i with 1/max_row
    for i in range(numrows):
        if (rowmulti[i] != 0):
            temp4 = array_b[i] * rowmulti[i]
            array_b[i] = temp4

    print ("\n---------------After Equilibration---------------\n")
    print ("A = \n", array_A, "\n-----------")
    print ("c = \n", array_c, "\n-----------")
    print ("b = \n", array_b, "\n-----------")

# ------------------Example of arrays to test Equilibration function------------------

# ------------------Example 1------------------
A1 = [  [100, -5, 3, 200],
        [20, -100, 4, 8],
        [12, -10, 10, 4],
        [-8, 80, 4, 14] ]
c1 = [ -10, 30, -20, 50 ]
b1 = [  [10],
        [20],
        [30],
        [40] ]

A1 = np.array(A1, dtype=float)
c1 = np.array(c1, dtype=float)
b1 = np.array(b1, dtype=float)

# ------------------Example 2------------------
A2 = [  [100, -50, 50, 20],
        [10, 5000, 25, -2000],
        [200, -100, 100, -50],
        [1000, 250, -50, -100] ]
c2 = [ 50, -100, 50, -25 ]
b2 = [  [100],
        [200],
        [300],
        [400] ]

A2 = np.array(A2, dtype=float)
c2 = np.array(c2, dtype=float)
b2 = np.array(b2, dtype=float)

# ------------------Example 3------------------
A3 = [  [24, -87, 635, -9810, -475, 658, 248, -55, 324, -98, 87, -320, 735, 79, -654],
        [453, 75, 452, -99, 753, 739, -741, 208, 74, 2035, 7853, 12, -478, 9573, 410],
        [298, -308, 71, 185, -4796, 5237, 1284, -9723, 4138, 795, 4381, 4932, 1298, -864, 1487],
        [1021, -479, 341, 285, 796, -35, 53, 1896, 348, -720, -5895, 6723, 842, 7935, -7328] ]
c3 = [ 211, 798, 384, -70, -945, 783, 257, 96, -207, 321, -742, 83, 944, 567, -667 ]
b3 = [  [741],
        [983],
        [55],
        [-411] ]

A3 = np.array(A3, dtype=float)
c3 = np.array(c3, dtype=float)
b3 = np.array(b3, dtype=float)

# ------------------Example 4------------------
A4 = [  [-5092, -4324, 6417, 1351, -4068, 4185, -7871, 1471, -2381, 2908, 3476, -3760, 401, -8936, -4322, 6819, 8218, 8499, -6674, 860],
        [-606, -4106, -2943, 851, -3603, 4817, 3701, -6358, 5893, 1618, -6885, 2325, 1351, 2373, -545, 3964, 1635, -1226, 2296, -8676],
        [-3695, 3566, -4002, -8891, 845, -3744, -8414, 8498, 5343, 3102, -2860, 8667, -2265, -6752, 8773, 8688, -7704, 961, 2901, -4861],
        [4588, 4510, -4943, 5186, 3735, -2158, -6048, 4334, -2080, -1188, 7146, 4503, -2735, -2309, 4006, 5445, 1589, 4915, 2725, 7497] ]
c4 = [2779, -2693, -1123, 4592, -5587, 6280, 282, -3669, 4229, -6271, 4789, 3525, 2996, -2432, -6373, -2251, -8427, -1861, -8744, -5772]
b4 = [  [741],
        [983],
        [55],
        [-411] ]

A4 = np.array(A4, dtype=float)
c4 = np.array(c4, dtype=float)
b4 = np.array(b4, dtype=float)


Equilibration(A1, c1, b1)
Equilibration(A2, c2, b2)
Equilibration(A3, c3, b3)
Equilibration(A4, c4, b4)
