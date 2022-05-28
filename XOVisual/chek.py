import controller as con

def check_win(smb):
    for n in range(3):
        check_line(con.field[n][0], con.field[n][1], con.field[n][2], smb)
        check_line(con.field[0][n], con.field[1][n], con.field[2][n], smb)
    check_line(con.field[0][0], con.field[1][1], con.field[2][2], smb)
    check_line(con.field[2][0], con.field[1][1], con.field[0][2], smb)


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False
