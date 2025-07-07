from Figura import *
import Funkcje



class Wieza(Figura):

    def __str__(self):
        return '♖ ' if self.kolor == "white" else '♜ '

    def ruch(self, szachownica, wiersz, kolumna, wiersz_koniec, kolumna_koniec):
        krok = 1 if wiersz_koniec > wiersz or kolumna_koniec > kolumna else - 1
        dostep = None
        if wiersz_koniec == wiersz:
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

        elif kolumna_koniec == kolumna:
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
        if dostep:
            szachownica[wiersz_koniec][kolumna_koniec] = Wieza(self.kolor)
            szachownica[wiersz][kolumna] = Funkcje.backup(wiersz, kolumna)
        else:
            print('Nie możesz pójść na to miejsce!')