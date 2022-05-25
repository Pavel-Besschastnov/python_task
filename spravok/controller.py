import record_tel
import search_tel
import user_interface
import logger
import output_stile

def run():
    temp = user_interface.choice()
    if temp == 1:
         print ('Вами выбрана операция внесения в справочник нового контакта')
        
         entry =  () # Запись в справочник
         logger.log_to_file(record_tel.recordtry)
         
    if temp == 2:
         print ('Вами выбрана операция поиска контакта в справочнике' )
         entry = search_tel.search() # Поиск в справочнике
         logger.reading_file(entry)

    if temp == 3:
         print ('Вами выбрана операция вывода на печать всех контактов справочника')
         logger.read_all_file()  