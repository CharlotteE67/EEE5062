import numpy as np
# load target matrix
A = np.array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]])
B = np.array([[2, 3, 4, 5, 6], [4, 4, 5, 6, 7], [0, 3, 6, 7, 8], [0, 0, 2, 8, 9], [0, 0, 0, 1, 0]])
H_6 = np.array([[1, 1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6], [1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7],
                [1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8],
                [1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9], [1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9, 1 / 10],
                [1 / 6, 1 / 7, 1 / 8, 1 / 9, 1 / 10, 1 / 11]])

# # get eigen values by numpy.linalg.eig() function
# # the function returns eigen values and vectors in order, choose first item to print
# eigen_A = np.linalg.eig(A)
# print(eigen_A[0])  # [3.02886853e+01 3.85805746e+00 1.01500484e-02 8.43107150e-01]
# eigen_B = np.linalg.eig(B)
# print(eigen_B[0])  # [13.1723514   6.55187835  1.59565457 -0.39078805 -0.92909628]
# eigen_H_6 = np.linalg.eig(H_6)
# print(eigen_H_6[0])  # [1.61889986e+00 2.42360871e-01 1.63215213e-02 6.15748354e-04 1.25707571e-05 1.08279948e-07]


# QR method
# def eigen_qr(matrix, eps=1e-7):
#     # define iteration and limitation
#     matrix_k = matrix
#     while True:
#         matrix_k_1 = matrix_k
#         q_k, r_k = np.linalg.qr(matrix_k)  # using np.linalg.qr() for qr decomposition
#         matrix_k = np.dot(r_k, q_k)
#         if np.sum(np.diag(np.abs(matrix_k - matrix_k_1))) < eps:
#             # when sum of elements in diagonal is less than limit, stop iteration
#             break
#     return np.diag(matrix_k)
#
#
# print(eigen_qr(A))
# print(eigen_qr(B))
# print(eigen_qr(H_6))