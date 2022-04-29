# 30 задача
# Вычислить число c заданной точностью d
# Пример: при d = 0.001, П = 3.141. 10-1d≤10-10
import random
import math
pi = math.pi
print('Число пи = ',pi)
d = 0.00001
print(f'Точность = {d}')
count = 0
while d < 1:
    count += 1
    d = d  *10
print(round(pi,count))

