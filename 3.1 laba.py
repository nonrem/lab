import math

def calculate_y(x, a, b):
    num = 1 + a * (x + b)
    denom = 3 + math.cos(a * x)
    if denom == 0:
        return float('inf')
    return num / denom

a = 3.9
b = 2.3
x1 = 1
xn = 6
dx = 0.2

print("Результаты (цикл for):")
for i in range(int((xn - x1) / dx) + 1):
    x = x1 + i * dx
    y = calculate_y(x, a, b)
    print(f"x = {x:.2f}, y = {y}")