# Задача 18
# Реализовать алгоритм перемешивания списка. 

import random
list = []
d = int(input('Введите размер списка :' ))
for i in range(d ):
    list.append(random.randint(1,100))
print(f'Создан список : \n {list}')
for i in range(d):
    s = random.randint(0,d-1)
    temp = list[i]
    list[i] = list[s]
    list[s] = temp
print(list)
