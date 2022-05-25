from datetime import datetime
import output_stile

def log_to_file(entry):  # Запись в файл
    b = output_stile.stile()   
    if b == 1:    
        with open('telefon.csv', 'a') as file:
            file.write(
                f'{datetime.today()};{entry[0]};{entry[1]};{entry[2]};{entry[3]};\n')

    if b == 2:
        with open('telefon.csv', 'a') as file:
            file.write(
                f'{datetime.today()}\n;{entry[0]}\n;{entry[1]}\n;{entry[2]}\n;{entry[3]};\n')    

def reading_file(param): # Чтение из файла
    with open('telefon.csv', 'r') as file:
        for line in file:
            if param in line:
                stroka = line
                print(line)

def read_all_file(): # Чтение всего справочника
    with open('telefon.csv', 'r') as file:
        for line in file:
            print(line)    
