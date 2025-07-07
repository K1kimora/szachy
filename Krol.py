from Figura import *
import Funkcje

class Krol(Figura):

    def __str__(self):
        return '♔ ' if self.kolor == "white" else '♚ '

    def ruch(self, szachownica, wiersz, kolumna, wiersz_koniec, kolumna_koniec):
        if abs(wiersz_koniec - wiersz) <= 1 and abs(kolumna_koniec - kolumna) <= 1:
            if isinstance(szachownica[wiersz_koniec][kolumna_koniec], str) or (not isinstance(szachownica[wiersz_koniec][kolumna_koniec], str) and szachownica[wiersz_koniec][kolumna_koniec].kolor != self.kolor):
                szachownica[wiersz_koniec][kolumna_koniec] = Krol(self.kolor)
                szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
        else:
            print('Nie możesz pójść na to miejsce!')