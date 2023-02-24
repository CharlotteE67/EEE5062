import numpy as np

# Q1
def p_linear(x):
    return 1.82321 * x - 1.604752

def p_erci(x):
    return -1.408500 * x * x + 3.372560*x -2.027302

def p(x):
    x1 = 0.6
    y1 = -0.510826
    x2 = 0.7
    y2 = -0.356675
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(k, b)
    return k * x + b

print(p_linear(0.59))
print(p_erci(0.59))
print(p_linear(0.64))
print(p_erci(0.64))
print(p(0.64))
# y1 = -0.693147
# y2 = -0.510826
# y3 = -0.356675
#
# delta1 = y2 - y1
# delta2 = y3 - y2
#
# delta = delta2 - delta1
#
# print(delta1, delta2, delta)

# Q4
# x1, x2, x3 = 1, 1, 1
# res = []
# new_1, new_2, new_3 = 0, 0, 0
# precision = 1e-3
# for i in range(10):
#     new_1 = -0.4 * x2 - 0.2 * x3 - 2.4
#     new_2 = 0.25 * new_1 - 0.5 * x3 + 1.8
#     new_3 = -0.2 * new_1 + 0.3 * new_2 + 0.3
#     res.append([new_1, new_2, new_3])
#     print(np.abs(new_1 - x1), np.abs(new_2 - x2), np.abs(new_3 - x3))
#     if np.abs(new_1 - x1) < precision and np.abs(new_2 - x2) < precision and np.abs(new_3 - x3) < precision:
#         break
#     x1, x2, x3 = new_1, new_2, new_3
# print("final:", new_1, new_2, new_3)

# Q5
# A_1 = [[3, -4, 3], [-4, 6, 3], [3, 3, 1]]
# u_0 = [[1], [1], [1]]
# A_1 = np.array(A_1)
# u_0 = np.array(u_0)
# u_k_1 = u_0
# for k in range(1, 20):
#     print(k)
#     v_k = np.dot(A_1, u_k_1)
#     u_k = v_k / max(v_k)
#     # print(u_k, v_k, max(v_k))
#     print(list(u_k.T))
#     print(max(v_k)[0])
#     u_k_1 = u_k
