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

print("Результаты (цикл while):")
x = x1
i = 0
while i <= int((xn - x1) / dx):
    y = calculate_y(x, a, b)
    print(f"x = {x:.2f}, y = {y}")
    x = x1 + (i + 1) * dx
    i += 1