import gauss_module
import numpy

a = numpy.array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype=float)

b = numpy.array([5, 6, 7, 8], dtype=float)

print(gauss_module.gauss(a, b))