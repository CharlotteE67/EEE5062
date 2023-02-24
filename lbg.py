import math


def f(x):
    # return 2 / (math.pi ** 0.5) * math.e ** (-x)
    return 1 / x


#
#
# a = 0
# b = 1
# t = []
# t.append(0.5 * (f(0) + f(1)))
# for i in range(1, 10):
#     div = 0.5 ** i
#     tmmm = f(div)
#     base = div
#     while base + 2 * div < 1:
#         base += 2 * div
#         tmmm += f(base)
#     tmp = 0.5 * t[len(t) - 1] + div * tmmm
#     t.append(tmp)
#
# s = []
# for i in range(9):
#     s.append(4/3*t[i+1]-1/3*t[i])
#
# c = []
# for i in range(8):
#     c.append(16/15*s[i+1]-1/15*s[i])
#
# r = []
# for i in range(7):
#     r.append(64/63*c[i+1]-1/63*c[i])
#
# print(t)
# print(s)
# print(c)
# print(r)
# print(r[1]-r[0])
# print(r[2]-r[1])

def lbg(a, b, f):
    t = []
    t.append(0.5 * (f(a) + f(b)))
    for i in range(0, 10):
        h = (b - a) / (2 ** i)
        sum = 0
        div = 0.5 ** i
        base = a + div * (b - a)
        tmmm = f(base)
        while base + 2 * div * (b - a) < b:
            # print(i, base)
            base += 2 * div * (b - a)
            tmmm += f(base)
        tmp = 0.5 * t[len(t) - 1] + div * (b - a) / 2 * tmmm
        t.append(tmp)

    s = []
    for i in range(9):
        s.append(4 / 3 * t[i + 1] - 1 / 3 * t[i])

    c = []
    for i in range(8):
        c.append(16 / 15 * s[i + 1] - 1 / 15 * s[i])

    r = []
    for i in range(7):
        r.append(64 / 63 * c[i + 1] - 1 / 63 * c[i])

    return t, s, c, r


t, s, c, r = lbg(1, 3, f)
print(t)
print(s)
print(c)
print(r)

# def erciyuan(a, b, c):
#     return (-b+(b*b-4*a*c)**0.5)/2*a, (-b-(b*b-4*a*c)**0.5)/2*a
#
# a, b = erciyuan(1, -9/14, -3/70)
# print(a, b)
# print(2*(1+a)/(3*(b-a)), -2*(b+1)/(3*(b-a)))