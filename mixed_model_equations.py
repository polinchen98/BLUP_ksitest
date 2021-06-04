import numpy as np
import scipy.linalg as la
from matrix_A_inv_np import get_inversion_matrix_A_ignore_inbreeding


def constructing_mixed_model_equations(pedigree):

    X = []

    for key in pedigree.keys():
        sex = pedigree[key]['sex']
        if sex is not None:
            X.append([int(sex), (int(sex) + 1) % 2])
    X = np.matrix(X)
    X_trans = X.T

    string_Z = []
    position_of_one = 0

    for key in pedigree.keys():
        sire = pedigree[key]['sire']
        dam = pedigree[key]['dam']
        array = np.zeros(len(X))

        if sire is not None or dam is not None:
            array[position_of_one] = 1
            position_of_one += 1

        string_Z.append(array)

    Z = np.matrix(string_Z).T
    Z_trans = Z.T

    y = []
    for key in pedigree.keys():
        wwg = pedigree[key]['WWG']
        if wwg is not None:
            y.append(wwg)

    X_trans_Z = np.dot(X_trans, Z)
    Z_trans_X = np.dot(Z_trans, X)

    X_trans_X = np.dot(X_trans, X)
    Z_trans_Z = np.dot(Z_trans, Z)

    X_trans_y = (np.dot(X_trans, y)).T
    Z_trans_y = (np.dot(Z_trans, y)).T

    A_inv = get_inversion_matrix_A_ignore_inbreeding(pedigree)

    A_inv_alpha = A_inv * 2
    sum_Z_A = Z_trans_Z + A_inv_alpha

    matrix_1 = np.vstack((np.hstack((X_trans_X, X_trans_Z)), np.hstack((Z_trans_X, sum_Z_A))))
    matrix_2 = np.vstack((X_trans_y, Z_trans_y))

    solution = np.dot(la.inv(matrix_1), matrix_2)

    return solution
