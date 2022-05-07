# Задача 35
# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
#  A[i] - 1 = A[i-1]. Найти его.
import os
import io
with open('task35Num.txt', 'r') as f:
    text = str(f.read())
print('В файле имеется следующая последовательность чисел:\n', text)
list = text.split(' ')
list = [num for num in list if num.isdigit()]
list2 = []
for a in range(1, len(list)):
    list2.append(list[a - 1])
    if int(list[a]) - 1 != int(list[a - 1]):
        list2.append(int(list[a]) - 1)
        print('В последовательности не хватает числа:', (int(list[a]) - 1))

print('Исправленный список:\n', list2)
