str = input('Введите строку: ')
counter = str.count('а')
l = len(str)
rep = str.replace('а', 'о')
print(f'Измененная строка: {rep}\nКоличество замен: {counter}\nСимволов в строке: {l}')