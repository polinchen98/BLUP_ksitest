import math


def get_inversion_matrix_A_accounted_inbreeding(pedigree):
    L = [[0 for row in range(len(pedigree) + 1)] for col in range(len(pedigree) + 1)]
    D_inv = [[0 for row in range(len(pedigree) + 1)] for col in range(len(pedigree) + 1)]
    A_inv = [[0 for row in range(len(pedigree) + 1)] for col in range(len(pedigree) + 1)]

    # for matrix L
    for i in range(1, len(L)):
        for j in range(1, i + i):
            sire = pedigree[i]['sire']
            dam = pedigree[i]['dam']

            if i == j:

                summ_l_s = 0
                summ_l_d = 0

                if sire is not None:
                    for m in range(1, sire + 1):
                        summ_l_s += L[sire][m] ** 2

                if dam is not None:
                    for m in range(1, dam + 1):
                        summ_l_d += L[dam][m] ** 2

                L[i][i] = math.sqrt((1 - 0.25 * (summ_l_s + summ_l_d)))

            if sire is not None and sire >= j:
                L[i][j] = 0.5 * L[sire][j]

            if dam is not None and dam >= j:
                L[i][j] += 0.5 * L[dam][j]

    # for matrix D_inv

    for i in range(1, len(D_inv)):
        for j in range(1, i + i):
            D_inv[i][i] = 1 / L[i][i] ** 2

    for i in range(len(D_inv)):
        print(D_inv[i][i])

    # for matrix A_inv

    for i in range(1, len(A_inv)):

        sire = pedigree[i]['sire']
        dam = pedigree[i]['dam']
        diagonal_element = D_inv[i][i]

        if sire is not None and dam is not None:
            A_inv[i][i] += diagonal_element

            A_inv[sire][i] += -diagonal_element / 2
            A_inv[i][sire] += -diagonal_element / 2
            A_inv[dam][i] += -diagonal_element / 2
            A_inv[i][dam] += -diagonal_element / 2

            A_inv[sire][dam] += diagonal_element / 4
            A_inv[dam][sire] += diagonal_element / 4
            A_inv[sire][sire] += diagonal_element / 4
            A_inv[dam][dam] += diagonal_element / 4

        elif sire is not None and dam is None:
            A_inv[i][i] += diagonal_element

            A_inv[sire][i] += -diagonal_element / 2
            A_inv[i][sire] += -diagonal_element / 2

            A_inv[sire][sire] += diagonal_element / 4
        else:
            A_inv[i][i] = diagonal_element

    return A_inv



