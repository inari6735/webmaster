
from peewee import *

baza_plik = 'quiz.db'
############## MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza


class Pytanie(BazaModel):
    pytanie = CharField(null=False, unique=True)

class Odpowiedz(BazaModel):
    pytanie = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpowiedz = CharField(null=False)
    odpok = BoleanField(default=False)
