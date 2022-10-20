# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]

# Создаю список из случайных чисел
import random
print('Введите число')
n = int(input())
lst = []
for i in range(n):
    num = random.randint(1, 100)
    lst.append(num)
print(lst)

# Создаю новый список
lst_new = []
for i in range(len(lst)):
    while i < len(lst)/2 and n > len(lst)/2:
        n = n - 1
        a = lst[i] * lst[n]
        lst_new.append(a)
        i += 1
print(lst_new)


