from multiplication_matrix import multiply_matrix
from transponse_matrix import transpose_matrix
from matrix_D import get_inversion_D_ignore_inbreeding


def get_inversion_matrix_A(matrix_D_inv, matrix_T_inv):
    matrix_T_inv_trans = transpose_matrix(matrix_T_inv)
    A_inv_1 = multiply_matrix(matrix_T_inv_trans, matrix_D_inv)
    A_inv = multiply_matrix(A_inv_1, matrix_T_inv)
    return A_inv


# if ignoring inbreeding


def get_inversion_matrix_A_ignore_inbreeding(pedigree):
    A_inv = [[0 for row in range(len(pedigree) + 1)] for col in range(len(pedigree) + 1)]
    D_inv = get_inversion_D_ignore_inbreeding(pedigree)

    for i in range(1, len(A_inv)):

        sire = pedigree[i]['sire']
        dam = pedigree[i]['dam']

        if sire is not None and dam is not None:
            A_inv[i][i] += D_inv[i][i]

            A_inv[sire][i] += (-D_inv[i][i]) / 2
            A_inv[i][sire] += (-D_inv[i][i]) / 2
            A_inv[dam][i] += (-D_inv[i][i]) / 2
            A_inv[i][dam] += (-D_inv[i][i]) / 2

            A_inv[sire][dam] += D_inv[i][i] / 4
            A_inv[dam][sire] += D_inv[i][i] / 4
            A_inv[sire][sire] += D_inv[i][i] / 4
            A_inv[dam][dam] += D_inv[i][i] / 4

        elif sire is not None and dam is None:
            A_inv[i][i] += D_inv[i][i]

            A_inv[sire][i] += - D_inv[i][i] / 2
            A_inv[i][sire] += - D_inv[i][i] / 2

            A_inv[sire][sire] += D_inv[i][i] / 4
        else:
            A_inv[i][i] = D_inv[i][i]

    return A_inv

