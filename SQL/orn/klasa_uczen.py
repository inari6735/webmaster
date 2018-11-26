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
    klasa = ForeignKeyField(Klasa, related_name='wyniki')

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl1 = Klasa(nazwa='2A', roknaboru=2012, rokmatury=2015)
    kl2 = Klasa(nazwa='1A', roknaboru=2013, rokmatury=2016)
    kl3 = Klasa(nazwa='3A', roknaboru=2011, rokmatury=2014)
    u1 = Uczen(imie='Cezary', nazwisko='Pazura', plec=False, klasa=kl1)
    u2 = Uczen(imie='Agnieszka', nazwisko='Adamska', plec=True, klasa=kl2)
    u3 = Uczen(imie='Andrzej', nazwisko='Grabowski', plec=False, klasa=kl3)
    kl1.save()
    kl2.save()
    kl3.save()
    u1.save()
    u2.save()
    u3.save()
    
    uczniowie = Uczen.select()
    
    for uczen in uczniowie:
        print(uczen.id, uczen.imie, uczen.nazwisko)
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
