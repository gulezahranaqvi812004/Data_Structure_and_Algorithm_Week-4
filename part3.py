Cdef partialMatrix(A, startingIndex, rows, columns):
    row_start, col_start = startingIndex
    partial_matrix = []

    for row in range(row_start, row_start + rows):
        row_values = []
        for col in range(col_start, col_start + columns):
            row_values.append(A[row][col])
        partial_matrix.append(row_values)

    return partial_matrix


def addMat(A, B):

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return 0


    result = [[0 for a in range(len(A[0]))] for b in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):

            result[i][j] = A[i][j] + B[i][j]

    return result
def addSubmatrices(A,B,start, size):
    subMatrixA=partialMatrix(A,start,size,size)
    subMatrixB=partialMatrix(B,start,size,size)
    partialSum=addMat(subMatrixA,subMatrixB)
    return partialSum

def multiplyMatrix(A,B,start,size):

   x_start,y_start=start
   rows=size
   cols=size
   result = []

   for i in range(x_start, x_start + rows):
        row = []
        for j in range(y_start, y_start + cols):
            row.append(A[i][j] + B[i][j])
            result.append(row)

   return result
def printMatrix(A):
    for row in A:
        print(row)


# A1 = [ [1, 2, 3],
#     [4, 5, 6],]
#
# B = [[7, 8, 9],
#     [10, 11, 12],]
#
#
# result = addMat(A1, B)
# printMatrix(result)
#
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]
# printMatrix(partialMatrix(matrix,(1,2),2,3))


mul1 = [
    [1, 2, 3, 4, 5],
    [2, 2, 2, 2, 2],
    [3,3,3,3,3],
    [4,4,4,4,4]
]

mul2 = [
    [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

printMatrix(multiplyMatrix(mul1,mul2,(1,2),2))
