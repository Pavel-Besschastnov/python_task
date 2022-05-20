# 41. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

stroka = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
data = open('text41.txt', 'w')
data.write(stroka)
data.close
path = 'text41.txt'
data = open(path, 'r')
str_old = data.read()
data.close
def compress(str_old):
    str_new = ''
    count = 1
    for e in range(len(str_old) - 1):
        if str_old[e + 1] == str_old[e]:
            count += 1
        else:
            str_new += str(count) + str_old[e]
            count = 1
    str_new += str(count) + str_old[e]
    return str_new
with open('compres41.txt', 'w') as data:
    data.write(compress(str_old))

with open('compres41.txt', 'r') as data:
    comp_stroka = data.read()
def decompress(comp_stroka):
    decomp_stroka = ''
    char_qty = ''
    for i in range(len(comp_stroka)):
        if comp_stroka[i].isdigit():
            char_qty += comp_stroka[i]
        else:
            decomp_stroka += comp_stroka[i] * int(char_qty)
            char_qty = ''
    return decomp_stroka
with open('final41.txt', 'w') as data:
    data.write(decompress(comp_stroka))
