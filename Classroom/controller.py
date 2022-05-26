import db_operations as db
import ui


def run():
    data = db.get_base()
    print(data)
    menu = ['Просмотр базы;Добавление сведений']
    choice = ui.get_choice(menu[0])
    if choice == 1:
        print(*get_data())
        db_operations()
    elif choice == 2:
        db.add_data()
    else:
        print('Ошибка ввода!')
