# Задача
# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел
s = 0
from datetime import datetime
while s < 10:
    d = datetime.now()
    s = int(d.second)
    
a = int(input('Введите количество цифр в числе :'))
count = 1
d = 1
while count <= a:
    d = d * 10
    count = count + 1
if a == 1:
    s = s % 10 
    print(f' Случайное число = {s}')
elif a > 1:
    s = s ** 326 + a * 363616762343231
    s = s % d
print(f'Случайное число = {s }')
