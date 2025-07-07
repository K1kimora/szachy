from Figura import *
import Funkcje


class Skoczek(Figura):

    def __str__(self):
        return '♘ ' if self.kolor == "white" else '♞ '

    def ruch(self, szachownica, wiersz, kolumna, wiersz_koniec, kolumna_koniec):
        if (abs(wiersz_koniec - wiersz) == 2 and abs(kolumna_koniec - kolumna) == 1) or (abs(wiersz_koniec - wiersz) == 1 and abs(kolumna_koniec - kolumna) == 2):
            if not isinstance(szachownica[wiersz_koniec][kolumna_koniec], str):
                if szachownica[wiersz_koniec][kolumna_koniec].kolor != self.kolor:
                    szachownica[wiersz_koniec][kolumna_koniec] = Skoczek(self.kolor)
                    szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
            else:
                szachownica[wiersz_koniec][kolumna_koniec] = Skoczek(self.kolor)
                szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)