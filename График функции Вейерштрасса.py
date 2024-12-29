import numpy as np
import matplotlib.pyplot as plt

def weierstrass(x, a=0.5, b=3, n=20):
    sum = 0
    for i in range(n):
        sum += a**i * np.cos(b**i * np.pi * x)
    return sum

a = 0.5
b = 3
n = 50
x_min = -2
x_max = 2
num_points = 500

x = np.linspace(x_min, x_max, num_points)
y = weierstrass(x, a, b, n)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title(f'Функция Вейерштрасса (a={a}, b={b}, n={n})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()