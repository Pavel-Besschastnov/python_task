# Задача 38
# Напишите программу, удаляющую из текста все слова содержащие "абв"
b = 'абввав слово вваава смаабв ддыдл ваввл дллабв аорс абввв'
print('Введен некий текст:\n ', b)
b = list(b.split(' '))
print('Удаление всех слов содержащих "абв"\n')
for i in range(0, len(b)):
    if i > len(b):
        break
    elif b[i].find('абв') != -1:
        b.pop(i)
a = ''
for i in range(len(b)):
    a = a + ' ' + str(b[i])
print('Текст без лишних слов:\n ', a)
