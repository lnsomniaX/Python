import math
import numpy as np
import cmath
import matplotlib.pyplot as plt

ITERATIONS = 5


def my_cosh(x):
    """
    Вычисление гиперболического косинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x ** 2  # В цикле постепенно считаем степень
        multiplier *= 1 / (2 * n - 1) / (2 * n)  # (-1)^n и факториал
        partial_sum += x_pow * multiplier

    return partial_sum


help(math.cosh)
help(my_cosh)

complex_arg = cmath.acosh(5)

print('Аргумент, при котором cosh достигает пяти', complex_arg)
print("Достигает ли пяти наш cosh?", my_cosh(complex_arg))
print("А библиотечный?", cmath.cosh(complex_arg))

p = np.r_[-2:2:0.01]
y = my_cosh(p)

plt.subplot(1, 2, 1)
plt.grid()
plt.plot(p, y, label='my_cosh')
plt.plot(p, np.cosh(p), label='np.cosh', linestyle='dotted')
plt.legend(fontsize=8,
           ncol=2,
           facecolor='#f8f8ff',
           edgecolor='black',
           title_fontsize='8')
plt.title('cosh при -2≤x≤2')

p = np.r_[-10:10:0.01]
y = my_cosh(p)

plt.subplot(1, 2, 2)
plt.plot(p, y, label='my_cosh')
plt.plot(p, np.cosh(p), label='np.cosh', linestyle='dotted')
plt.grid()
plt.legend(fontsize=8,
           ncol=2,
           facecolor='#f8f8ff',
           edgecolor='black',
           title_fontsize='8')
plt.title('cosh при -10≤x≤10')
plt.show()
