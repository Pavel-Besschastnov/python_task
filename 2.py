# Задача 2
# Найти максимальное из пяти чисел

list = [2,23,343,3,90]
max = list[0]
for i in range(len(list)):
    if max < list[i] : max = list[i]
print(f" Максимальное число из данных : {max}")
