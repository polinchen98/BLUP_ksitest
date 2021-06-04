import numpy as np


def get_numerator_relationship_matrix(pedigree):

    A = np.zeros(((len(pedigree)), len(pedigree)))

    for i in range(len(A)):
        for j in range(i+1):
            sire = pedigree[i+1]['sire']
            dam = pedigree[i+1]['dam']
            if sire is not None and dam is not None:
                if i == j:
                    A[i][i] = 1 + 0.5 * A[sire-1][dam-1]
                else:
                    A[i][j] = A[j][i] = 0.5 * (A[j][sire-1] + A[j][dam-1])
            elif sire is not None and dam is None:
                if i == j:
                    A[i][i] = 1
                else:
                    A[i][j] = A[j][i] = 0.5 * A[j][sire-1]
            else:
                if i == j:
                    A[i][i] = 1
                else:
                    A[i][j] = 0

    return A
