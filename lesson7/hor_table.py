import csv
import log

def hor(a, b, c, d):
    with open('horizont_table.csv', 'a') as horizont_table:
        horizont_writer = csv.writer(horizont_table)
        horizont_writer.writerow([a, b, c, d])
        log.log_to_file(a,b,c,d)



