#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py

import sqlite3

def kwerenda(cur):
    cur.execute("""
        WITH srednie AS(
        SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie
        INNER JOIN oceny ON uczniowie.id = oceny.id_uczen
        GROUP BY uczniowie.id
        ) SELECT nazwisko, imie, sred FROM srednie
        WHERE sred > 3.5 ORDER BY sred DESC
    """)
    # WHERE pled = 1
    # SELECT id FROM uczniowie WHERE imie = 'Anna' AND nazwisko = 'Ignaczuk'
    # % dowolny ciąg znaków, dowolnej długości
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

def main(args):
    # KONFIGURACJA #########
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
