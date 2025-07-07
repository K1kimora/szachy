def backup(wiersz, kolumna):
    return '⬜️' if (wiersz + kolumna) % 2 == 0 else '⬛️'


def wys_board(board):
    print('   0  1  2  3   4  5   6   7')
    j = 0
    for i in board:
        print(j, '', end='')
        print(*i)
        j += 1
