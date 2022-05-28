from tkinter import*
import bot
import chek

root = Tk()
root.title('Крестики-Нолики')
game_run = True
field = []
cross_count = 0


def run():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        chek.check_win('X')
        if game_run and cross_count < 5:
            bot.computer_move()
            chek.check_win('O')





for row in range(3):
    line = []
    for col in range(3):
        button = Button(root,
                        text=' ',
                        width=6,
                        height=4,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='Новая игра!', command=run)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
