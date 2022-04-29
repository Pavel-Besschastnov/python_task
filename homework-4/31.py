# 31 задача
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
import random
n = random.randint(10,100)
print(f'Натуральное число  N = {n}')
spisok = []
while n > 1:
    for i in range(2,n + 1):
        if n % i == 0:
            n = int(n / i)
            spisok.append(i)
            break

print(f'Список простых множителей числа N = {spisok}')


