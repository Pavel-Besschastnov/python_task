import controller as c
import bot as b
import chek as ch


def click(row, col):
    if c.game_run and c.field[row][col]['text'] == ' ':
        c.field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        ch.check_win('X')
        if c.game_run and cross_count < 5:
            b.bot_move()
            ch.check_win('O')
