import matplotlib.pyplot as plt

# x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
# y = [0, 1.27, 2.16, 2.86, 3.44, 3.87, 4.15, 4.37, 4.51, 4.58, 4.62, 4.64]
#
# pair = []
# for i in range(len(x)):
#     pair.append([x[i], y[i]])
#
# plt.plot(x, y, 'ro')
# plt.plot(x, y)
#
# plt.xlabel('Time t/s')
# plt.ylabel('Concentration y/(x10^-4)')
# plt.show()
x = [0, 0.9, 1.9, 3.0, 3.9, 5.0]
y = [0, 10, 30, 50, 80, 110]

pair = []
for i in range(len(x)):
    pair.append([x[i], y[i]])

plt.plot(x, y, 'ro')
plt.plot(x, y)

plt.xlabel('Time t/s')
plt.ylabel('Distance s/m')
plt.show()