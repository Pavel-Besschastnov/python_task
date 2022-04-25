# Задача 23
# Найти произведение пар чисел в списке.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
import random
spisok =[]
a = int(input("Введите длину списка :"))
for i in range(a):
    spisok.append(random.randint(1,10))
print(f"Создан новый список: \n {spisok}")
newspisok =[]
l = a - 1
for i in range(a):
     if i == l + 1 and a % 2 == 0:
        break
     newspisok.append(spisok[i] * spisok[l])
     if i == l and a % 2 != 0:
        break
     l -=1
print(newspisok)
