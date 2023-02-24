import numpy as np

a = np.array([[0.37, 0.33], [0.33, 0.34]])
# a = np.array([[19801, 19602], [19602, 19405]])
# print(np.linalg.eig(a))
# print(0.68534073 ** 0.5)
# value, vector = np.linalg.eig(a)
# print(max(value), min(value))
# print((max(value)/min(value))**0.5)
b = np.array([[2,1,1],[1,2,1],[1,1,2]])
print(np.linalg.eig(b))