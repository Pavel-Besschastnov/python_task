# Задача 17
# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
import random
import os

d = 10  #int(input("Введите количество чисел в списке :"))
# list = []
# for i in range(d):
#     list.append(random.randint(-d, d))
# print(list)
# f = open('task17.txt', 'w')
# f.close()
# list2 = []
# for i in range(int(d / 3)):
#     list2.append(random.randint(0, d))
# print(list2)
# f = open('task17.txt', 'w')

# for index in list2:  # Запись списка с индексами в файл
#     f.writelines("%s\n" % index)
# f.close()
# count = 1
# a = len(list2) + 1
# f = open('task17.txt')
# for lis in f.readlines():  # перебираем индексы из файла
#     s = int(lis)
#     count = count * list[s]

# f.close()
# print(f'произведение элементов : {count}')
firsttext = [i for i in range(-d, d + 1)]
print(firsttext)
pos = [random.randint(0, d) for i in range(int(d / 3))]
print(f'Следующие индексы будут записаны в файл: {pos}')
with open('firsttext.txt', 'w') as f1:
    for i in range(len(pos)):
        f1.writelines(str(pos[i]) + '\n')

with open('firsttext.txt') as f1:
    fin = list(f1.readlines())
x = 1
for i in range(len(fin)):
    x = x * int(fin[i])
print(f'Произведения элементов по указанным индексам = {x}')
