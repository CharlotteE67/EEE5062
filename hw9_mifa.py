import numpy as np

A_1 = [[7, 3, -2], [3, 4, -1], [-2, -1, 3]]
u_0 = [[1], [1], [1]]
A_1 = np.array(A_1)
u_0 = np.array(u_0)
u_k_1 = u_0
for k in range(1, 8):
    print(k)
    v_k = np.dot(A_1, u_k_1)
    u_k = v_k / max(v_k)
    # print(u_k, v_k, max(v_k))
    print(list(u_k.T))
    print(max(v_k)[0])
    u_k_1 = u_k