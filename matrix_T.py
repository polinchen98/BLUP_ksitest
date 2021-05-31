def get_lower_triangular_matrix(pedigree):

    T = [[0 for row in range(len(pedigree) + 1)] for col in range(len(pedigree) + 1)]

    for i in range(1, len(T)):
        for j in range(1, i + 1):
            sire = pedigree[i][0]
            dam = pedigree[i][1]
            if i == j:
                T[i][i] = 1
            elif sire is not None and dam is not None:
                T[i][j] = T[j][i] = 0.5 * (T[j][sire] + T[j][dam])
            elif sire is not None and dam is None:
                T[i][j] = T[j][i] = 0.5 * T[j][sire]
            else:
                T[i][j] = 0
    return T
