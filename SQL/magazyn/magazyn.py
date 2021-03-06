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


def main(args):
    nazwa_bazy = 'magazyn'
    
    dane_z_pliku(nazwa_bazy + '.db')
    exit()

    con = sqlite3.connect('tabela.db')
    cur = con.cursor()  # utworzenie kursora

    with open(nazwa_bazy + 'sql', 'r') as plik:
        cur.executescript(plik.read())

    dane = dane_z_pliku('dane_customers.txt')
    print(dane)
    return
    dane.pop(0)
    cur.executemany(
    'INSERT INTO ' + nazwa_bazy + 'VALUES(?, ?, ?, ?, ?)', dane)
    
    con.commit()  # zatwierdzenie wszystkich operacji w bazie
    con.close() # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
