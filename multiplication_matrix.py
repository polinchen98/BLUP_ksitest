def multiply_matrix(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        print('Impossible to take action!')
    else:
        matrix_c = [[0 for row in range(len(matrix_b[0]))] for col in range(len(matrix_a))]

        for i in range(len(matrix_a)):
            for j in range(len(matrix_b[0])):
                for k in range(len(matrix_a[0])):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

        return matrix_c
