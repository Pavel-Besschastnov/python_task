import db_operations as db
import add_data as ad
import ui


def run():
    
    
    while True:
        choice = ui.get_choice()
        if choice == 1:
            print(db.get_data())                     
        elif choice == 2:
            ad.add_data()
        elif choice == 3:
            print('Программа завершена!')
            exit()