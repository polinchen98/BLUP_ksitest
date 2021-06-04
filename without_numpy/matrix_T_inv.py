def get_inversion_matrix_T(pedigree):

    matrix_I = [[0 for row in range(len(pedigree) + 1)] for col in range(len(pedigree) + 1)]
    matrix_M = [[0 for row in range(len(pedigree) + 1)] for col in range(len(pedigree) + 1)]
    matrix_T_inv = [[0 for row in range(len(matrix_I))] for col in range(len(matrix_I))]

    # for matrix I
    for i in range(1, len(matrix_I)):
        for j in range(1, i + 1):
            if i == j:
                matrix_I[i][i] = 1
            else:
                matrix_I[i][j] = 0

    # for matrix M
    for i in range(1, len(matrix_M)):
        for j in range(1, i+1):
            sire = pedigree[i]['sire']
            dam = pedigree[i]['dam']
            if sire is not None and dam is not None:
                matrix_M[i][sire] = 0.5
                matrix_M[i][dam] = 0.5
            elif sire is not None and dam is None:
                matrix_M[i][sire] = 0.5
            else:
                matrix_M[i][j] = 0

    # for matrix T_inv
    for i in range(len(matrix_T_inv)):
        for j in range(len(matrix_T_inv[0])):
            matrix_T_inv[i][j] = matrix_I[i][j] - matrix_M[i][j]

    return matrix_T_inv



