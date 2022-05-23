import os
import read_export
import hor_table
import vert_table
import tel_info


def start():
    print('Добро пожаловать в телефонный справочник!')
    print('Выберите режим работы :')
    print(f'1 Запись в файл построчно.\n2 Запись в файл столбцом.\n3 Прочитать файл с строками и экспортировать его.\n4 Прочитать файл с столбцами и его экспорт.')
    while True:
        reg = int(input())
        if reg < 0 or reg > 4:
            print('Выбран неверный режим! Введите правильный!')
            continue
        break
    if reg == 1:
        a, b, c, d = tel_info.telef()
        vert_table.vert(a, b, c, d)
    elif reg == 2:
        a, b, c, d = tel_info.telef()
        hor_table.hor(a, b, c, d)
    elif reg == 3:
        read_export.read_exp()
        ex = input('Желаете экспортировать данные? ( y/n ) : ')
        if ex == 'y':read_export.read_exp()
    elif reg == 4:
        read_export.read_exp()
        ex = input('Желаете экспортировать данные? ( y/n ) : ')
        if ex == 'y':read_export.read_exp()



        
        
        

        

start()
