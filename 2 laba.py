import math

def f_x(x, func_choice):
    match func_choice:
        case 1:
            return math.sinh(x)
        case 2:
            return x**2
        case 3:
            return math.exp(x)
        case _:
            return None

try:
    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    func_choice = int(input("Выберите вид функции f(x): sh(x) -> 1, x**2 -> 2, e**x -> 3 \n -> "))

    fx = f_x(x, func_choice)

    if fx is None:
        raise ValueError("Неверный выбор функции")


    if x - y == 0:
        c = fx**2 + y**(1/3) + math.sin(y)
    elif x - y > 0:
        c = (fx - y)**2 + math.log(x)
    elif x - y < 0:
        c = (y - fx)**2 + math.tan(y)
    else:
        raise ValueError("Неопределенное условие")


    print(f"Результат: {c}")

except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла неожиданная ошибка: {e}")