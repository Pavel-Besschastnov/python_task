from tkinter import *
import clik as cl


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


for row in range(3):
    line = []
    for col in range(3):
        button = Button(root,
                        text=' ',
                        width=4,
                        height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: cl.click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='Новая игра!', command= run)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
