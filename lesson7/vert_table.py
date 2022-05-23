import csv

# Пишет в строку(())
def vert(a, b, c, d):
    with open('vertical_table.csv', 'a', newline='') as vertical_table:
        vertical_writer = csv.writer(vertical_table)
        vertical_writer.writerow([a, b, c, d])



vert()