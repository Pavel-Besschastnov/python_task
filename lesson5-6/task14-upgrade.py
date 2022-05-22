# 14 Задача
#  Подсчитать сумму цифр в вещественном числе
import os
import random as r
from pickle import TRUE
from unicodedata import digit

# n = input("Введите вещественное число :")
# count = 0
# for i in n:
#     if i.isdigit() == True:
#         count = count + 1

# print(f" количество цифр в числе = : {count}")

n = r.uniform(1, 10)
print(n)
spisok = list(map(int, str(n).replace('.', '')))
print('Сумма цифр данного числа равна:', sum(spisok), '\n')
