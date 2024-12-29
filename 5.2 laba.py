my_list = [10, 20, 5, 12, 30, 8, 15, 25]
modified_list = [x * 2 if x < 15 else x for x in my_list]
print("Исходный список:", my_list)
print("Модифицированный список:", modified_list)