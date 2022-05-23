import csv


def read_exp_H():
    with open('horizont_table.csv') as csv.file:
        csv_reader = csv.reader(csv.file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count+= 1
                print(f'\t{row[0]} {row[1]} {row[2]} {row[3]}')
        print(f'Обработано {line_count-1} строк.')

def read_exp_V():
    with open('vertical_table.csv') as csv.file:
        csv_reader = csv.reader(csv.file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count+= 1
                print(row)
        print(f'Обработано {line_count-1} строк.')

def export_V():
    with open('vertical_table.csv') as csv.file:
        csv_reader = csv.reader(csv.file, delimiter=',')
        with open('exportV.csv','w') as f:
            vertical_writer = csv.writer(f,lineterminator='\n')
            for row in csv_reader:
                f.write(str(row))
                f.writelines('\n')

def export_H():
    with open('horizont_table.csv') as csv.file:
        csv_reader = csv.reader(csv.file, delimiter=',')
        with open('exportH.csv','w') as f:
            vertical_writer = csv.writer(f,lineterminator='\n')
            for row in csv_reader:
                f.write(str(row))
                f.writelines('')