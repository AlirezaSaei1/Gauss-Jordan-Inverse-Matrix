def inverse(matrix, n):
    # Row Interchange
    for i in range(n):
        # matrix[i][i] == 0
        if abs(matrix[i][i]) < 1.0e-12:
            for j in range(i+1, n):
                if abs(matrix[j][i]) > abs(matrix[i][i]):
                    matrix[i], matrix[j] = matrix[j], matrix[i]

        pivot = matrix[i][i]
        if pivot == 0:
            print("Error: Zero Division Detected")
            return

        for j in range(i, 2*n):
            matrix[i][j] /= pivot

        for j in range(n):
            if i == j or matrix[j][i] == 0:
                continue
            factor = matrix[j][i]
            for k in range(i, 2*n):
                matrix[j][k] -= factor * matrix[i][k]
    return matrix


def printInverseMatrix(matrix, n):
    print("Inverse Matrix:")
    for a in matrix:
        print(*["{0:0.3f}".format(i) for i in a[n:]])


def printMatrix(matrix, a, b, label="Matrix"):
    # print first a rows and b columns of given matrix
    print(label + ":")
    for row in range(a):
        print(*matrix[row][:b])


def add_identity_matrix(matrix, n):
    # make n*n matrix to n*2n (Matrix + Identity Matrix)
    aug_matrix = [[0 for _ in range(2*n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            aug_matrix[i][j] = matrix[i][j]

            if i == j:
                aug_matrix[i][j + n] = 1
    return aug_matrix


def readFromFile(address):
    M = []
    with open(address, 'r') as file:
        for line in file.readlines():
            M.append(list(map(int, line.split())))
        return M


matrix = readFromFile("Matrix1.txt")
n = len(matrix)
printMatrix(matrix, n, n, "Matrix")
print("------------------------")
id_matrix = add_identity_matrix(matrix, n)
printMatrix(id_matrix, n, 2*n, "Extended Matrix")
print("------------------------")
inverse_matrix = inverse(id_matrix, n)
printMatrix(inverse_matrix, n, 2*n, "Function Result")
print("------------------------")
printInverseMatrix(inverse_matrix, n)
print("------------------------")