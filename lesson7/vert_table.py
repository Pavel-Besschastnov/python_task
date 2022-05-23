import csv

# Пишет в строку(())
def vert_table(a, b, c, d):
    with open('vertical_table.csv', 'a', newline='') as vertical_table:
        vertical_writer = csv.writer(vertical_table)
        vertical_writer.writerow([a, b, c, d])


a = 'sdsd'
b = 'sdad'
c = 'ss'
d = 'saasdsafsf'
vert_table(a, b, c, d)
