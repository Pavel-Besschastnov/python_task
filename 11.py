# Задача 11
# Сформировать список из  N членов последовательности.
#  Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = int(input("Введите любое положительное число :"))
#while N == 
list = []
v = int(1) # временная переменная
for i in range(1,N+1):
    list.append(v)
    v = v * (-3)
    
print ( list)