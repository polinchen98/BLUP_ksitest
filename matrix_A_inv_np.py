import numpy as np


def get_inversion_matrix_A_ignore_inbreeding(pedigree):
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

    A_inv = np.zeros(((len(pedigree)), len(pedigree)))

    for i in range(len(A_inv)):
        sire = pedigree[i+1]['sire']
        dam = pedigree[i+1]['dam']
        if sire is not None and dam is not None:
            A_inv[i][i] += v[i]

            A_inv[sire-1][i] += -v[i] / 2
            A_inv[i][sire-1] += -v[i] / 2
            A_inv[dam-1][i] += -v[i] / 2
            A_inv[i][dam-1] += -v[i] / 2

            A_inv[sire-1][dam-1] += v[i] / 4
            A_inv[dam-1][sire-1] += v[i] / 4
            A_inv[sire-1][sire-1] += v[i] / 4
            A_inv[dam-1][dam-1] += v[i] / 4

        elif sire is not None and dam is None:
            A_inv[i][i] += v[i]

            A_inv[sire-1][i] += - v[i] / 2
            A_inv[i][sire-1] += - v[i] / 2

            A_inv[sire-1][sire-1] += v[i] / 4
        else:
            A_inv[i][i] += v[i]

    return A_inv
