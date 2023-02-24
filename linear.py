x = [0.4, 0.5, 0.6, 0.7, 0.8]
y = [-0.916291, -0.693147, -0.510826, -0.356675, -0.223144]

# for i in range(len(x)):
#     for j in range(i+1, len(x)):
#         k = (y[j] - y[i]) / (x[j] - x[i])
#         b = y[i] - k * x[i]
#         pre = (0.54 - x[i]) * k + y[i]
#         print('Range:', x[i], x[j], 'k =', k, 'predicted =', pre, b)
one = 1
two = 2
tri = 3

l1 = y[one] / ((x[one] - x[two]) * (x[one] - x[tri]))
l2 = y[two] / ((x[two] - x[one]) * (x[two] - x[tri]))
l3 = y[tri] / ((x[tri] - x[one]) * (x[tri] - x[two]))
a = l1 + l2 + l3
b = -(x[two] + x[tri]) * l1 - (x[two] + x[one]) * l3 - (x[one] + x[tri]) * l2
c = x[two] * x[tri] * l1 + x[one] * x[tri] * l2 + x[one] * x[two] * l3
# print(0.916291/0.02)
# print(l1, l2, l3)
print(a, b, c)
print(a * 0.54 * 0.54 + b * 0.54 + c)
