# Задача 16
# Задать список из n чисел последовательности  и вывести на экран их сумму

n = int(input("Введите число  :"))


def pos(o):
    p = (1 + 1 / o)**o
    return p


list = []
for i in range(1, n + 1):
    list.append(round(pos(i), 3))
print(f"Последовательность из n чисел = {list}")
sum = 0
for i in range(n):
    sum = sum + list[i]
print(f" Сумма из n чисел в списке = {sum} ")