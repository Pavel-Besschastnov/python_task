# Задача 8
# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

print(" Введите координату Х :")
x = int(input())
print(" Введите координату Y :")
y = int(input())

if x == 0 and y == 0:
    print("Точка координат находится на пересечении оси координат.")
elif x == 0 and (y > 0 or y < 0):
    print("Точка находится на Оси Y." )
elif y == 0 and (x > 0 or x < 0):
    print("Точка находится на Оси X." )
elif x > 0 and y > 0:
    print("Точка координат находится в первой четверти.")
elif x > 0 and y < 0:
    print("Точка координат находится в второй четверти.")
elif x < 0 and y < 0:
    print("Точка координат находится в третьей четверти.")
elif x < 0 and y > 0:
    print("Точка координат находится в четвертой четверти.")