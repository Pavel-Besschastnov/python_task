
 #  40. *Создайте программу для игры в "Крестики-нолики". 


from re import X


d = [1,2,3,4,5,6,7,8,9 ]
count = 0
X = "X"
for i in range(0,3):
    print(f' {d[i*3]} {d[i*3+1]} {d[i*3+2]}') # Рисуем табличку
while count < 9:
    t = "Крестика " if X == "X" else "Нолика "
    while True:    # Проверяем правильно ли введено число
        n = int(input(f'Введите число ячейки для {t}'))
        if n > 10 or n < 1 or not (n in d):
            print('Введите другое число')
            continue
        break
    d[n-1] = X
    for i in range(0,3):
        print(f' {d[i*3]} {d[i*3+1]} {d[i*3+2]}') # Печать промежуточного этапа
    count+= 1
    X = "X" if X != "X" else"O"
    r = ""
    for i in range(0,2): # Проверка линий на совпадение
        if d[3*i] == d[3*i+1] and d[3*i+1] == d[3*i+2]:
            r = d[3*i]
        if d[i] == d[3+i] and d[3+i] == d[6+i]:r = d[i]
        if d[0] == d[4] and d[4] == d[8]:r = d[0]
        if d[2] == d[4] and d[4] == d[6]:r = d[2]
        if r =="" and count > 8:
            print("Ничья")
            break
        if r !="" :
            print(f'{"Крестики" if r == "X" else "Нолики"} выиграли')
            break

