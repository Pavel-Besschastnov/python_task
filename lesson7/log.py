
from datetime import datetime


def log_to_file(a,b,c,d):
    with open('log.csv', 'a') as file:
        file.write(
            f'{datetime.today()};{a};{b};{c};{d};\n')