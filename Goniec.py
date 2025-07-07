from Figura import *
import Funkcje


class Goniec(Figura):

    def __str__(self):
        return '♗ ' if self.kolor == "white" else '♝ '

    def ruch(self, szachownica, wiersz, kolumna, wiersz_koniec, kolumna_koniec):
        krok = 1 if wiersz_koniec > wiersz else - 1
        dostep = None
        y = kolumna + 1 if kolumna_koniec > kolumna else kolumna - 1
        if abs(wiersz_koniec - wiersz) == abs(kolumna_koniec - kolumna):
            for i in range(wiersz + krok, wiersz_koniec + krok, krok):
                if isinstance(szachownica[i][y], str):
                    dostep = True
                else:
                    if szachownica[i][y].kolor == self.kolor:
                        dostep = False
                        break
                    elif szachownica[i][y].kolor != self.kolor:
                        if i == wiersz_koniec:
                            dostep = True
                        else:
                            dostep = False
                            break
                y += 1 if kolumna_koniec > kolumna else - 1
            if dostep:
                szachownica[wiersz_koniec][kolumna_koniec] = Goniec(self.kolor)
                szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
            else:
                print('Nie możesz pójść na to miejsce!')