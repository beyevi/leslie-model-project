"""
Python module to find eigenvalues and eigenvectors
using the QR-factorisation
"""


import numpy as np


def find_eigenvalues(matrix, iters=500000):
    """
    Find eigenvalues of a given matrix using QR decomposition
    """
    eigenvalues = []

    Ak = np.copy(matrix)
    n = matrix.shape[0]
    QQ = np.eye(n)

    for k in range(iters):
        Q, R = np.linalg.qr(Ak)
        Ak = R @ Q
        QQ = QQ @ Q

    for i in range(n):
        eigenvalues.append(Ak[i, i])

    return eigenvalues


def find_eigenvectors(matrix):
    """
    Find eigenvectors of a given matrix corresponding to each its eigenvalue
    """

#     n = A.shape[0]
#     I = np.eye(n)
#
#     eigenvecs = []
#
#     for eigenvalue in eigenvals:
#         x = np.random.rand(n)  # Random initial guess for eigenvector
#         for _ in range(max_iter):
#             evc = np.linalg.solve(A - eigenvalue * I, x)  # Solve (A - eigenvalue*I)x = 0
#             evc /= np.linalg.norm(evc)  # Normalize eigenvector
#             if np.linalg.norm(A @ evc - eigenvalue * evc) < tol:  # Check convergence
#                 eigenvecs.append(evc)
#                 break
#             x = evc  # Update initial guess for next iteration
#
#     return eigenvecs

    return np.linalg.eig(matrix)[1]


if __name__ == "__main__":
    A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]], dtype=float)

    ev = find_eigenvalues(A)
    evc = find_eigenvectors(A)

    print(ev)
    print(evc)
