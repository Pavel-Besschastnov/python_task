import db_operations as db
import add_data as ad
import ui


def run():
    data = db.get_data()
    print(data)
    menu = ['Просмотр базы;Добавление сведений; Выход']
    choice = ui.get_choice(menu[0])
    if choice == 1:
        print(db.get_data())
        ui.get_choice(menu[0])
    elif choice == 2:
        ad.add_data()
        ui.get_choice(menu[0])
    elif choice == 3:
        print('Программа завершена!')
        exit()
    else:
        print('Ошибка ввода!')
