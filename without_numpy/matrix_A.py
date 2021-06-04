def get_numerator_relationship_matrix(pedigree):

    A = [[0 for row in range(len(pedigree)+1)] for col in range(len(pedigree)+1)]

    for i in range(1, len(A)):
        for j in range(1, i+1):
            sire = pedigree[i]['sire']
            dam = pedigree[i]['dam']
            if sire is not None and dam is not None:
                if i == j:
                    A[i][i] = 1 + 0.5 * A[sire][dam]
                else:
                    A[i][j] = A[j][i] = 0.5 * (A[j][sire] + A[j][dam])
            elif sire is not None and dam is None:
                if i == j:
                    A[i][i] = 1
                else:
                    A[i][j] = A[j][i] = 0.5 * A[j][sire]
            else:
                if i == j:
                    A[i][i] = 1
                else:
                    A[i][j] = 0

    return A
