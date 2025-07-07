from Figura import *
import Funkcje



class Hetman(Figura):

    def __str__(self):
        return '♕ ' if self.kolor == "white" else '♛ '

    def ruch(self, szachownica, wiersz, kolumna, wiersz_koniec, kolumna_koniec):
        dostep = None
        y = kolumna + 1 if kolumna_koniec > kolumna else kolumna - 1
        if wiersz_koniec == wiersz and abs(kolumna_koniec - kolumna) != 0:
            krok = 1 if wiersz_koniec > wiersz or kolumna_koniec > kolumna else - 1
            for i in range(kolumna + krok, kolumna_koniec + krok, krok):
                if isinstance(szachownica[wiersz][i], str):
                    dostep = True
                else:
                    if szachownica[wiersz][i].kolor == self.kolor:
                        dostep = False
                        break
                    elif szachownica[wiersz][i].kolor != self.kolor:
                        if i == kolumna_koniec:
                            dostep = True
                        else:
                            dostep = False
                            break
                y += 1 if kolumna_koniec > kolumna else - 1

        elif kolumna_koniec == kolumna and abs(wiersz_koniec - wiersz) != 0:
            krok = 1 if wiersz_koniec > wiersz or kolumna_koniec > kolumna else - 1
            for i in range(wiersz + krok, wiersz_koniec + krok, krok):
                if isinstance(szachownica[i][kolumna], str):
                    dostep = True
                else:
                    if szachownica[i][kolumna].kolor == self.kolor:
                        dostep = False
                        break
                    elif szachownica[i][kolumna].kolor != self.kolor:
                        if i == wiersz_koniec:
                            dostep = True
                        else:
                            dostep = False
                            break
        elif abs(wiersz_koniec - wiersz) == abs(kolumna_koniec - kolumna):
            krok = 1 if wiersz_koniec > wiersz and kolumna_koniec > kolumna else - 1
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
            szachownica[wiersz_koniec][kolumna_koniec] = Hetman(self.kolor)
            szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
        else:
            print('Nie możesz pójść na to miejsce!')