def transpose_matrix(matrix):
    transposed = [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

    return transposed



