# Задача 20
# Определить, присутствует ли в заданном списке строк, некоторое число 

spisok = ('moon', 'man', 'string', '123', 'door', 'table', '23', 'sdsd', 'spoon')
count = 0
for i in spisok:
    if i.isdigit() == True:
        print(f'В списке есть число: {i}')
        count = count + 1
    
        if count == 0: print(f'В списке нет числа.')
print(spisok)