import csv
from email.headerregistry import SingleAddressHeader
from ossaudiodev import SNDCTL_DSP_SETSPDIF
from socket import ALG_SET_AEAD_ASSOCLEN
import log


def vert(a, b, c, d):
    with open('vertical_table.csv', 'a', newline='') as vertical_table:
        spisok = list([a,b,c,d])
        log.log_to_file(a,b,c,d)
        vertical_writer = csv.writer(vertical_table,lineterminator='\n')
        for var in spisok:
            vertical_writer.writerow([var])
        vertical_table.writelines('\n')
        




