import numpy as np

def CSC(arr):
    
    # Counter for the number of non zeros
    count = 0

    # Number of rows and columns
    numrows = len(arr)
    numcols = len(arr[0])

    # Create arrays
    Anz = []
    JA = []
    IA = []
    Anz = np.array(Anz)
    JA= np.array(JA)
    IA= np.array(IA)

    # Counter for the number of columns that contain only zeros
    zero_rows = 0

    for i in range(numcols):
        # Flag that indicates if we have found the first non zero number for every column
        first_nnz = False
        # Flag that indicates if the number of non zeros has changed after the iteration of the column before
        temp = count

        for j in range(numrows):
            if (arr[j][i] != 0):
                count += 1
                Anz = np.append(Anz, [arr[j][i]])
                JA = np.append(JA, j+1)
                if (first_nnz == False):
                    # We have found the first non zero number for this column
                    first_nnz = True
                    if (zero_rows != 0):
                        for x in range(zero_rows+1):
                            IA = np.append(IA, count)
                            zero_rows = 0
                    elif (zero_rows == 0):
                        IA = np.append(IA, count)
                elif (first_nnz == True):
                    continue
        if (temp == count):
            zero_rows += 1
    # Add last element at the end of the IA array: (number of non zeros)+1
    IA = np.append(IA, count+1)

    print ("Anz = ", Anz)
    print ("JA = ", JA)
    print ("IA = ", IA)


matrix_A = [[0 for i in range(5)] for j in range(5)]
matrix_A = np.array(matrix_A)
matrix_A[0][1] = -4
matrix_A[1][0] = -2
matrix_A[1][2] = 1
matrix_A[2][2] = 1
matrix_A[3][1] = 1
matrix_A[3][4] = -5
matrix_A[4][3] = -9
print ("Array A:\n", matrix_A)

matrix_B = [[0 for i in range(6)] for j in range(6)]
matrix_B = np.array(matrix_B)
matrix_B[0][0] = 1
matrix_B[0][3] = 9
matrix_B[1][0] = 5
matrix_B[2][1] = -3
matrix_B[2][4] = 2
matrix_B[3][2] = 5
matrix_B[3][5] = -1
matrix_B[4][3] = 2
matrix_B[5][1] = 7
matrix_B[5][5] = 1
print ("\nArray B:\n", matrix_B)

# Array C is like array A but 3rd row has zeros only
matrix_C = [[0 for i in range(5)] for j in range(5)]
matrix_C = np.array(matrix_C)
matrix_C[0][1] = -4
matrix_C[1][0] = -2
matrix_C[1][2] = 1
matrix_C[3][1] = 1
matrix_C[3][4] = -5
matrix_C[4][3] = -9
print ("Array C:\n", matrix_C)

# Array D is like array B but 4th and 5th row have zeros only
matrix_D = [[0 for i in range(6)] for j in range(6)]
matrix_D = np.array(matrix_D)
matrix_D[0][0] = 1
matrix_D[0][3] = 9
matrix_D[1][0] = 5
matrix_D[2][1] = -3
matrix_D[2][4] = 2
matrix_D[5][1] = 7
matrix_D[5][5] = 1
print ("\nArray D:\n", matrix_D)

print ("\n-------------------CSC for A-------------------")
CSC(matrix_A)

print ("\n-------------------CSC for B-------------------")
CSC(matrix_B)

print ("\n-------------------CSC for C-------------------")
CSC(matrix_C)

print ("\n-------------------CSC for D-------------------")
CSC(matrix_D)
