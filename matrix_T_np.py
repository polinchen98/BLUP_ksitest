import numpy as np


def get_lower_triangular_matrix(pedigree):

    T = np.zeros(((len(pedigree)), len(pedigree)))

    for i in range(len(T)):
        for j in range(i+1):
            sire = pedigree[i+1][0]
            dam = pedigree[i+1][1]
            if i == j:
                T[i][i] = 1
            elif sire is not None and dam is not None:
                T[i][j] = T[j][i] = 0.5 * (T[j][sire-1] + T[j][dam-1])
            elif sire is not None and dam is None:
                T[i][j] = T[j][i] = 0.5 * T[j][sire-1]
            else:
                T[i][j] = 0
    return T

pedigree = {1: [None, None],
               2: [None, None],
               3: [1, 2],
               4: [1, None],
               5: [4, 3],
               6: [5, 2]}
matrix_T = (get_lower_triangular_matrix(pedigree))
print(matrix_T)
