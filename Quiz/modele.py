
from peewee import *

baza_plik = 'quiz.db'
############## MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza

class Kategoria(BazaModel):
    kategorie = CharField(null=False)

class Pytanie(BazaModel):
    pytanie  = CharField(null=False)
    kategorie = ForeignKeyField(Kategoria, related_name='pytania')
    
class Odpowiedz(BazaModel):
    odpowiedz = CharField(null=False)
    pytanie = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpok = IntegerField(default=0)

