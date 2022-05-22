# Задача 17
# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
import random
import os

d = int(input("Введите количество чисел в списке :"))
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
