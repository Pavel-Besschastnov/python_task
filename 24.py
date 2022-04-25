# Задача 24
# В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
import math
a = int(input("Введите длину желаемого списка:"))
list = []
for i in range(a):
    list.append(round(random.uniform(0,10),3))
print(list)
b = math.modf(list[1])
print(type(b))