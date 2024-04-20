"""
Python module to find eigenvalues and eigenvectors
using the QR-factorisation
"""


import numpy as np

import qr_factorization as qr


def find_eigenvalues(A, tol=1e-12, maxiter=1000):
    """
    Find eigenvalues of a given matrix using QR decomposition
    """
    A_old = np.copy(A)
    A_new = np.copy(A)
    
    diff = np.inf
    i = 0
    while diff > tol and i < maxiter:
        A_old[:, :] = A_new
        Q, R = qr.qr_decomposition(A_old)
        
        A_new[:, :] = R @ Q
        
        diff = np.abs(A_new - A_old).max()
        i += 1

    eigenvalues = np.diag(A_new)
    
    return eigenvalues


def find_eigenvectors(A, eigenvals, tol=1e-6, max_iter=1000):
    """
    Find eigenvectors of a given matrix corresponding to each its eigenvalue
    """
    n = A.shape[0]
    I = np.eye(n)

    eigenvecs = []

    for eigenvalue in eigenvals:
        x = np.random.rand(n)  # Random initial guess for eigenvector
        for _ in range(max_iter):
            evc = np.linalg.solve(A - eigenvalue * I, x)  # Solve (A - eigenvalue*I)x = 0
            evc /= np.linalg.norm(evc)  # Normalize eigenvector
            if np.linalg.norm(A @ evc - eigenvalue * evc) < tol:  # Check convergence
                eigenvecs.append(evc)
                break
            x = evc  # Update initial guess for next iteration

    return eigenvecs


if __name__ == "__main__":
    A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]], dtype=float)

    ev = find_eigenvalues(A)

    print(sorted(ev))
    print(np.linalg.eigvals(A))
    print(find_eigenvectors(A, ev))
