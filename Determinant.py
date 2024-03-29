from GaussJordan import printMatrix, readFromFile


def findRow(matrix):
    zeroCount = []
    for row in matrix:
        zeroCount.append(row.count(0))

    return zeroCount.index(max(zeroCount))


def subMatrix(matrix, row, col):
    new_matrix = []
    count = 0
    for r in matrix:
        if count != row:
            temp = r[:col] + r[col+1:]
            new_matrix.append(temp)
        count += 1
    return new_matrix


# Recursive Function To Calculate Matrix Determinant
def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    # find a row with maximum 0s in it
    index = findRow(matrix)
    # print(index)
    dt = 0
    for i in range(n):
        if matrix[index][i] != 0:
            sign = (-1) ** (i % 2)
            dt += sign * matrix[index][i] * \
                determinant(subMatrix(matrix, index, i), n-1)
    return dt


def upper_triangle_matrix(matrix, n):
    for k in range(n):
        for i in range(k+1, n):
            if matrix[k][k] == 0:
                matrix[k][k] == 1.0e-12

            sc = matrix[i][k] / matrix[k][k]

            # make elements 0
            for j in range(n):
                matrix[i][j] = matrix[i][j] - sc * matrix[k][j]
    return matrix


# Calculate Determinant via building Upper Triangle Matrix
def faster_determinant(matrix, n):
    M = upper_triangle_matrix(matrix, n)
    printMatrix(M, n, n, "Upper Triangle Matrix:")

    dt = 1
    for i in range(n):
        dt *= M[i][i]
    return dt


if __name__ == "__main__":
    matrix = readFromFile("Matrix1.txt")
    n = len(matrix)

    printMatrix(matrix, n, n, "Matrix")
    print("Determinant:", determinant(matrix, n))
    print("Faster Determinant:", faster_determinant(matrix, n))
