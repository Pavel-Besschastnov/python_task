import pobeda as pb
import random
import controller as c



def computer_move():
    for n in range(3):
        if pb.can_win(c.field[n][0], c.field[n][1], c.field[n][2], 'O'):
            return
        if pb.can_win(c.field[0][n], c.field[1][n], c.field[2][n], 'O'):
            return
    if pb.can_win(c.field[0][0], c.field[1][1], c.field[2][2], 'O'):
        return
    if pb.can_win(c.field[2][0], c.field[1][1], c.field[0][2], 'O'):
        return
    for n in range(3):
        if pb.can_win(c.field[n][0], c.field[n][1], c.field[n][2], 'X'):
            return
        if pb.can_win(c.field[0][n], c.field[1][n], c.field[2][n], 'X'):
            return
    if pb.can_win(c.field[0][0], c.field[1][1], c.field[2][2], 'X'):
        return
    if pb.can_win(c.field[2][0], c.field[1][1], c.field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if c.field[row][col]['text'] == ' ':
            c.field[row][col]['text'] = 'O'
            break
