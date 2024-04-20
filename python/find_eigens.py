"""
Python module to find eigenvalues and eigenvectors
using the QR-factorisation
"""


import numpy as np
from tabulate import tabulate


def find_eigenvalues(A, repeats=500000):
    Ak = np.copy(A)
    n = Ak.shape[0]
    QQ = np.eye(n)

    for k in range(repeats):
        s = Ak.item(n-1, n-1)
        smult = s * np.eye(n)

        Q, R = np.linalg.qr(np.subtract(Ak, smult))

        Ak = np.add(R @ Q, smult)
        QQ = QQ @ Q

        if k % 10000 == 0:
            print("A",k,"=")
            print(tabulate(Ak))
            print("\n")

    return Ak, QQ


if __name__ == "__main__":
    A = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    find_eigenvalues(A)
