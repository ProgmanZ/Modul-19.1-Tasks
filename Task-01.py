# Задача 1. Словарь квадратов чисел

num = int(input('Введите целое число: '))

quad_dict = {i: i**2 for i in range(1, num + 1)}

print('Результат:', quad_dict)
