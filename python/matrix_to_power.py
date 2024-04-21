"""
Python module for taking matrices to some power
using their diagonal or Jordan forms 
"""

import numpy as np

import find_eigens as eigen


def find_p_matrix(A):
    """
    Find matrix P (and its inverse) consisting of eigenvectors of a given matrix
    """
 
    eigenvals = eigen.find_eigenvalues(A)
    eigenvecs = eigen.find_eigenvectors(A, eigenvals)
    
    P = np.column_stack(eigenvecs)
    inv_P = np.linalg.inv(P)
    
    return P, inv_P


def to_power_diag(A, power):
    """
    Ascend matrix A to some given power using its diagonal decomposition
    """
    P, inv_P = find_p_matrix(A)
    eigenvals = eigen.find_eigenvalues(A)

    D_powered = np.diag(np.power(eigenvals, power))

    return np.dot(np.dot(P, D_powered), inv_P)


if __name__ == "__main__":
    A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]], dtype=float)
    print(to_power_diag(A, 5))
