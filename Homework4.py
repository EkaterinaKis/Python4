# 1. Вычислить число Пи c заданной точностью d
# при d = 0.001, π = 3.141, при d = 0.0001, π = 3.1415

# import math
# print(math.pi)
# num = float(input('Укажите точность числа: '))
# newpi = str(num)
# newpi = len(newpi[newpi.find('.')+1:])
# print(float(f'{math.pi:0.{newpi}f}'))

# 2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.
# 6 -> [2,3], 144 -> [2,3]

# num = int(input('Введите число: '))
# mass = []
# i = 2
# while num != 1:
#     while num % i == 0:
#         mass.append(i)
#         num //= i
#     i += 1
# print(mass)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
# a = [1, 5, 10, 5, 3, 15, 8, 9, 15, 9, 1, 11, 12]
# import random
# a = [random.randint(0, 5) for i in range(8)]
# print(a)
# print(set(a))