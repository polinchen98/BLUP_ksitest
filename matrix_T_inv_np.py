import numpy as np


def get_inversion_matrix_T(pedigree):

    matrix_I = np.eye((len(pedigree)))
    matrix_M = np.zeros((len(pedigree), len(pedigree)))
    matrix_T_inv = np.zeros((len(matrix_I), len(matrix_I)))

    # for matrix M
    for i in range(len(matrix_M)):
        for j in range(i+1):
            sire = pedigree[i+1][0]
            dam = pedigree[i+1][1]
            if sire is not None and dam is not None:
                matrix_M[i][sire-1] = 0.5
                matrix_M[i][dam-1] = 0.5
            elif sire is not None and dam is None:
                matrix_M[i][sire-1] = 0.5
            else:
                matrix_M[i][j] = 0

    # for matrix T_inv
    matrix_T_inv = matrix_I - matrix_M

    return matrix_T_inv
