#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=';')  # \t - tabulator
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]
            dane.append(rekord)
    return dane  # print(dane)


def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor()  # utworzenie kursora

    with open('szkola.sql', 'r') as plik:
        cur.executescript(plik.read())

    oceny = dane_z_pliku('szkoła_z6pr052010_oceny.txt')
    przedmioty = dane_z_pliku('szkoła_z6pr052010_przedmioty.txt')
    uczniowie = dane_z_pliku('szkoła_z6pr052010_uczniowie.txt')
    oceny.pop(0)  # usunięcie pierwszego elementu listy
    przedmioty.pop(0)  # usunięcie pierwszego elementu listy
    uczniowie.pop(0)  # usunięcie pierwszego elementu listy
    cur.executemany('INSERT INTO oceny VALUES(?, ?, ?, ?)', oceny)
    cur.executemany('INSERT INTO przedmioty VALUES(?, ?, ?, ?)', przedmioty)
    cur.executemany('INSERT INTO uczniowie VALUES(?, ?, ?, ?, ?, ?)', uczniowie)

    con.commit()  # zatwierdzenie wszystkich operacji w bazie
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
