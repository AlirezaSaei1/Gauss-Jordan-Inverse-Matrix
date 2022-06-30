def inverse(matrix, n):
    pass


def printMatrix(matrix, label):
    print(label + ": ")
    for row in matrix:
        print(*row)


def augmented_matrix(matrix, n):
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
printMatrix(matrix, "Matrix")
aug_matrix = augmented_matrix(matrix, n)
printMatrix(aug_matrix, "Augmented matrix")
