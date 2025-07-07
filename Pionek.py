from Figura import *
import random
from Skoczek import *
from Krol import *
from Hetman import *
from Goniec import *
from Wieza import *
import Funkcje


class Pionek(Figura):

    def __str__(self):
        return '♙ ' if self.kolor == "white" else '♟ '

    def ruch(self, szachownica, wiersz, kolumna, wiersz_koniec, kolumna_koniec):
        if (self.kolor == 'white' and wiersz == 1) or (self.kolor == 'black' and wiersz == 6):
            if abs(wiersz_koniec - wiersz) <= 2 and abs(kolumna_koniec - kolumna) == 0:
                szachownica[wiersz_koniec][kolumna_koniec] = Pionek(self.kolor)
                szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
        else:
            if abs(wiersz_koniec - wiersz) == 1:
                if abs(kolumna_koniec - kolumna) == 1 and not isinstance(szachownica[wiersz_koniec][kolumna_koniec], str):
                    if szachownica[wiersz_koniec][kolumna_koniec].kolor != self.kolor:
                        szachownica[wiersz_koniec][kolumna_koniec] = Pionek(self.kolor)
                        szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
                if isinstance(szachownica[wiersz_koniec][kolumna_koniec], str) and kolumna_koniec - kolumna == 0:
                    szachownica[wiersz_koniec][kolumna_koniec] = Pionek(self.kolor)
                    szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
            else:
                print('Nie możesz pójść na to miejsce!')
            if (self.kolor == 'white' and wiersz_koniec == 7) or (self.kolor == 'black' and wiersz_koniec == 0):
                randomowa_figura = random.choice((Skoczek(self.kolor), Wieza(self.kolor), Goniec(self.kolor), Hetman(self.kolor), Krol(self.kolor)))
                szachownica[wiersz_koniec][kolumna_koniec] = randomowa_figura
                szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)