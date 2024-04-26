"""
Python module for taking matrices to some power
using their diagonal or Jordan forms 
"""

import numpy as np

import find_eigens as eigen


def find_p_matrix(matrix):
    """
    Find matrix P (and its inverse) consisting of eigenvectors of a given matrix
    """
    eigenvectors = eigen.find_eigenvectors(matrix)

    P = eigenvectors
    inv_P = np.linalg.inv(P)

    return P, inv_P


def to_power_diag(matrix, power):
    """
    Ascend matrix A to some given power using its diagonal decomposition
    """
    P, inv_P = find_p_matrix(matrix)
    eigenvals = eigen.find_eigenvalues(matrix)

    eigenvals_powered = [ev ** power for ev in eigenvals]

    D_powered = np.diag(eigenvals_powered)

    return np.dot(np.dot(P, D_powered), inv_P)


if __name__ == "__main__":
    print("Leslie Matrix Usage Example (Predicting 10 Gens)".center(100, "="))
    n_0 = np.array([
        [45],
        [18],
        [11],
        [4]
    ])

    leslie_matrix = np.array([
        [0, 1, 1.5, 1.2],
        [0.8, 0, 0, 0],
        [0, 0.5, 0, 0],
        [0, 0, 0.25, 0]
    ], dtype=float)

    for k in range(1, 11):
        L_n = to_power_diag(leslie_matrix, k)

        n_k = np.dot(L_n, n_0)
        print(n_k, "\n")
