
def get_base():
    with open('pupils.csv', 'r') as pupils_file:
        pupils = [pupil.replace('\n', '').split(';') for pupil in pupils_file]
    with open('adress.csv', 'r') as adress_file:
        adress = [adress.replace('\n', '').split(';')
                  for adress in adress_file]
    with open('cabinets.csv', 'r') as cabinets_file:
        cabinetes = [cabinet.replace('\n', '').split(';')
                     for cabinet in cabinets_file]
    return [pupils, adress, cabinetes]


def get_new_data():
    result_list = get_data()
    id = int(len(result_list))
    string = ''
    string += str(id)+';'      # list[0] - это Id ученика)
    string += input('Введите Фамилию: ')+';'
    string += input('Введите Имя: ')+';'
    string += input('Введите Класс: ')+';'
    string += input('Введите Статус: ')+';'
    string += input('Введите Ряд: ')+';'
    string += input('Введите Номер парты: ')+';'
    string += input('Введите Город: ') + ';'
    string += input('Введите Улицу: ')+';'
    string += input('Введите Дом: ')+';'
    string += input('Введите Квартира: ')+';'
    string += input('Введите Примечание: ')+';'
    print('Добавляем ученика: ', string)
    push_data(string)


def summa(a):
    result = ''
    for i in range(3):
        result += a[i]
    return result.replace('\n', '')+'\n'


def get_data():
    with open('name.csv', 'r') as name:
        name = name.readlines()

    with open('class.csv', 'r') as classe:
        classe = classe.readlines()

    with open('adress.csv', 'r') as adress:
        adress = adress.readlines()
    list = [summa(i)for i in zip(name, classe, adress)]
    return list


def push_data(str):
    str = str.split(';')
    with open('name.csv', 'a') as name:
        for i in range(0, 5):
            name.write(str[i]+';')
        name.write('\n')
    with open('class.csv', 'a') as classe:
        classe.write(str[0]+';')
        for i in range(5, 7):
            classe.write(str[i]+';')
        classe.write('\n')
    with open('adress.csv', 'a') as adress:
        adress.write(str[0]+';')
        for i in range(7, 12):
            adress.write(str[i]+';')
        adress.write('\n')
