import csv


def read_exp():
    with open('horizont_table.csv') as csv.file:
        csv_reader = csv.reader(csv.file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                print(f'\t{row[0]} {row[1]} {row[2]} {row[3]}')
        print(f'Обработано {line_count} строки.')


read_exp()
