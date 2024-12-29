n = int(input("Введите количество элементов списка: "))

my_list = []
for i in range(n):
    while True:
        try:
            number = float(input(f"Введите элемент {i+1}: "))
            my_list.append(number)
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

sum_odd = 0
for i in range(1, len(my_list), 2):
    if i < len(my_list):
        sum_odd += my_list[i]


print("Список:", my_list)
print("Сумма элементов с нечётными индексами:", sum_odd)