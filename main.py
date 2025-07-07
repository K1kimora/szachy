from Pionek import *
from Krol import *
from Hetman import *
from Goniec import *
from Skoczek import *
from Wieza import *
from Funkcje import wys_board


def main():
    szachownica = [[Wieza('white'), Skoczek('white'), Goniec('white'), Hetman('white'), Krol('white'), Wieza('white'),
                    Skoczek('white'), Goniec('white')],
                   [Pionek('white')] * 8,
                   ['⬜️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️'],
                   ['⬛️', '⬜️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️', '⬜️'],
                   ['⬜️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️'],
                   ['⬛️', '⬜️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️', '⬜️'],
                   [Pionek('black')] * 8,
                   [Wieza('black'), Skoczek('black'), Goniec('black'), Hetman('black'), Krol('black'), Wieza('black'),
                    Skoczek('black'), Goniec('black')]]

    while True:
        wys_board(szachownica)
        start = input('Podaj miejsce figury, którą chcesz chodzić:\n')
        wiersz = int(start[0])
        kolumna = int(start[-1])
        koniec = input('Gdzie chcesz przestawić figurę?\n')
        wiersz_koniec = int(koniec[0])
        kolumna_koniec = int(koniec[-1])
        try:
            szachownica[wiersz][kolumna].ruch(szachownica, wiersz, kolumna, wiersz_koniec, kolumna_koniec)
        except AttributeError:
            print('Na tym miejscu nie stoi żadna figura!')

if __name__ == '__main__':
    main()