from matrix_A_np import get_numerator_relationship_matrix
import numpy as np


def get_diagonal_matrix(pedigree):
    matrix_A = get_numerator_relationship_matrix(pedigree)

    v = []
    for key in pedigree.keys():
        sire = pedigree[key]['sire']
        dam = pedigree[key]['dam']
        if sire is not None and dam is not None:
            F_s = matrix_A[sire][sire] - 1
            F_d = matrix_A[dam][dam] - 1
            v.append(0.5 - 0.25 * (F_s + F_d))
        elif sire is not None and dam is None:
            F_s = matrix_A[sire][sire] - 1
            v.append(0.75 - 0.25 * F_s)
        else:
            v.append(1)
    matrix_D = np.diag(v)

    return matrix_D


# if ignoring inbreeding

def get_inversion_D_ignore_inbreeding(pedigree):
    v = []
    for key in pedigree.keys():
        sire = pedigree[key]['sire']
        dam = pedigree[key]['dam']
        if sire is not None and dam is not None:
            v.append(2)
        elif sire is not None and dam is None:
            v.append(4 / 3)
        else:
            v.append(1)
    D_inv = np.diag(v)
    return D_inv
