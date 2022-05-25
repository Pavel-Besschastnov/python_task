def  record():
    entry=[]
    surname = input('Введите Фамилию: ')
    entry.append(surname)
    name = input('Введите Имя: ')
    entry.append(name)
    telefon = input('Введите номер телефона: ')
    entry.append(telefon)
    description = input('Введите описание контакта (личный, рабочий, домашний и т.д.): ')
    entry.append(description)
    print('Вами введена запись: ', entry)
    return entry
