def get_numerator_relationship_matrix(pedigree):

    A = [[0 for row in range(len(pedigree)+1)] for col in range(len(pedigree)+1)]

    for i in range(1, len(A)):
        for j in range(1, i+1):
            sire = pedigree[i][0]
            dam = pedigree[i][1]
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


pedigree = {1: [None, None],
               2: [None, None],
               3: [1, 2],
               4: [1, None],
               5: [4, 3],
               6: [5, 2]}
matrix_A = (get_numerator_relationship_matrix(pedigree))
