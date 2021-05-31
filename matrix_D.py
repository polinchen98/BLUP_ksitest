from matrix_A import get_numerator_relationship_matrix


def get_diagonal_matrix(pedigree):
    matrix_A = get_numerator_relationship_matrix(pedigree)
    D = [[0 for row in range(len(pedigree)+1)] for col in range(len(pedigree)+1)]

    for i in range(1, len(D)):
        for j in range(1, i+i):
            sire = pedigree[i][0]
            dam = pedigree[i][1]
            if sire is not None and dam is not None:
                F_s = matrix_A[sire][sire] - 1
                F_d = matrix_A[dam][dam] - 1
                D[i][i] = 0.5 - 0.25 * (F_s + F_d)
            elif sire is not None and dam is None:
                F_s = matrix_A[sire][sire] - 1
                D[i][i] = 0.75 - 0.25 * F_s
            else:
                D[i][i] = 1
        return D


def get_inversion_D(D):
    D_inv = D
    for i in range(1, len(D)):
        D_inv[i][i] = "%.3f" % (1 / D[i][i])
    return D_inv

# if ignoring inbreeding


def get_inversion_D_ignore_inbreeding(pedigree):
    D_inv = [[0 for row in range(len(pedigree)+1)] for col in range(len(pedigree)+1)]
    for i in range(1, len(D_inv)):
        for j in range(1, i+i):
            sire = pedigree[i][0]
            dam = pedigree[i][1]
            if sire is not None and dam is not None:
                D_inv[i][i] = 2
            elif sire is not None and dam is None:
                D_inv[i][i] = 4 / 3
            else:
                D_inv[i][i] = 1
    return D_inv

