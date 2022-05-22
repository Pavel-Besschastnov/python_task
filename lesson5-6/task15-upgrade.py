# 15 ЗАДАЧА
# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
import math

# def factor(n):  # Возвращает факториал числа n
#     if n == 0:
#         return 1
#     else:
#         return factor(n - 1) * n

5
d = int(input("Введите число n : "))
# spisok = []
# for i in range(1, d + 1):
#     spisok.append(factor(i))
# print(spisok)

spisok = [math.factorial(x) for x in range(1, d + 1)]
print(f'Для N = {d} набор произведений чисел от 1 до N: {spisok}')