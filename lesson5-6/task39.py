# Задача 39. Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"
import os
import random


def clear_screen():
    os.system('clear')


clear_screen()

print('Запуск конфетной игры!!')
candy = int(input('Сколько конфет разыгрываем? '))
choys = int(input('Сколько конфет можно брать за один ход? '))
print('Общее количество конфет :\n', candy, '\n Варианты игры:')
print('1 игрок против игрока\n2 игрок против бота\n3 игрок против умного бота')
b = int(input('Введите уровень сложности(1,2 или 3):'))
print('Вы выбрали ', b, ' вариант!')
pl = random.randint(1, 2)


def botsimple():
    global tes
    tes = random.randint(1, choys)
    return tes


def botbrain():
    global tes
    tes = candy % (choys + 1)
    if tes == 0:
        tes += 1
    return tes


def human():
    global tes
    tes = int(input('Сколько конфет хотите взять?'))
    return tes


while candy > 0:
    print('Осталось', candy, 'конфет.')
    pl += 1
    if pl % 2 == 0:
        print('Ходит 1 игрок')
        while True:
            play = int(input('Сколько конфет взять?'))
            if play > choys or play < 1 or play > candy:
                print('Введите другое число')
                continue
            break
        candy -= play
    else:
        print('Ходит 2 игрок')
        if b == 1:
            print(human())
            candy -= tes
        elif b == 2:
            tes = botsimple()
            while tes > choys:
                tes -= 1
            print('Бот взял', tes)
            candy -= tes
        elif b == 3:
            print(botbrain())
            candy -= tes
if pl % 2 == 0:
    print('Победил 1 игрок')
else:
    print('Победил 2 игрок')
