#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')  # \t - tabulator
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]
            dane.append(rekord)
    return dane  # print(dane)


def kwerenda1(cur):
    cur.execute("""
        SELECT name AS nazwa, genre AS gatunek FROM filmy
    """)

    wyniki = cur.fetchall()
    for rekord in wyniki:
        print(rekord)


def main(args):
    dane_z_pliku('filmy.txt')
    exit()

    con = sqlite3.connect('filmy.db')
    cur = con.cursor()  # utworzenie kursora

    with open('filmy.sql', 'r') as plik:
        cur.executescript(plik.read())

    kwerenda1(cur)

    con.commit()  # zatwierdzenie wszystkich operacji w bazie
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
