#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py

import os
from peewee import *

############ MODEL
baza_plik = 'test_orm.db'
baza = SqliteDatabase(baza_plik)
class BazaModel(Model): # Model to obiekt zainportowany z peewee
    class Meta:
        database = baza
        
class Klasa(BazaModel): # przejęcie tego co zostało zapisane w BazaModel czyli class Meta: itd
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
class Wynik(BazaModel):
    egz_hum = DecimalField(default=0)
    egz_mat = DecimalField(default=0)
    egz_jez = DecimalField(default=0)
    

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
