# Задача 21
# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
list =  ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
s = 0
g = 'йцу'
for i in range(len(list)):
    if list[i] == g:
         s = s + 1
    if s == 2: 
        print(f'Второе вхождение "{g}" на позиции  {i}')
        break
if s < 2: print("ответ:-1")
