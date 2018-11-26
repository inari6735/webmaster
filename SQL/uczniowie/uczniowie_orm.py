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
    rok_naboru = IntegerField(default=0)
    rok_matury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
class Przedmiot(BazaModel):
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField
    
class Ocena(BazaModel):
    datad = DateField()
    ocena = DecimalField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    
    kl1 = Klasa(nazwa='2A', rok_naboru=2010, rok_matury=2013)
    kl1.save()
    
    u1 = Uczen(imie='Cezary', nazwisko='Pazura', plec=False, klasa=kl1)
    u1.save()
    
    p1 = Przedmiot(przedmiot='matematyka', imie_naucz='Bogusław', nazwisko_naucz='Linda', plec_naucz=False)
    p1.save()
    
    o1 = Ocena(datad='12-10-2015', ocena=5, uczen=u1, przedmiot=p1)
    o1.save()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
