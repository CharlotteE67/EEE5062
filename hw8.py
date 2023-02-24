import numpy as np

def diedai(x_k):
    #newton
    return (2*x_k*x_k*x_k+1) / (3*x_k*x_k-3)

def f(x):
    return x*x*x-3*x-1

def xianjie(x_k, x_k_1):
    return x_k - ((x_k - x_k_1) * f(x_k)) / (f(x_k) - f(x_k_1))

# newton
# x_0 = 2
# x_1 = diedai(x_0)
# x_2 = diedai(x_1)
# x_3 = diedai(x_2)
# print(x_1, x_2, x_3)
# print(np.abs(x_2 - 1.87938524))
# print(np.abs(x_3 - 1.87938524))

# xianjie
x_0 = 2
x_1 = 1.9
x_2 = xianjie(x_1, x_0)
x_3 = xianjie(x_2, x_1)
print(x_1, x_2, x_3)
print(np.abs(x_2 - 1.87938524))
print(np.abs(x_3 - 1.87938524))