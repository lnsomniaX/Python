import numpy


def gauss(a, b):
    a = a.copy()
    b = b.copy()

    def forward():
        n = len(a)
        m = len(a[0])

        c = numpy.zeros((n, m + 1))

        for i in range(n):
            c[i, m] = b[i]
            for j in range(m):
                c[i, j] = a[i, j]

        i = 0
        g = []
        for j in range(0, m):
            k = i
            while c[k, j] == 0:
                while c[k, j] < 0:
                    k += 1
            if k <= n:
                g.append(j)
                d = c[i, j]
                c[i, j] = c[k, j]
                c[k, j] = d
                i += 1
                for l in range(i, n):
                    c[l] = c[l] - c[i - 1] * c[l, j] / c[i - 1, j]
        return (c, g)

    def backward():
        c, g = forward()
        print(c, g)
        n = len(a)
        m = len(a[0])
        x = numpy.zeros(n, dtype=float)
        x[n - 1] = c[n - 1, m] / c[n - 1, m - 1]

        for i in reversed(range(n - 1)):
            sum = 0
            for j in range(g[i] + 1, n):
                sum += c[i, j] * x[j]
            x[i] = (c[i, m] - sum) / c[i, i]
        return x

    x = backward()
    return x


print(__name__, "was imported")
