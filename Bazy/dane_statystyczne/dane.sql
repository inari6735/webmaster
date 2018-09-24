CREATE TABLE miasta(
id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
nazwa_miasta TEXT(30),
wojewodztwo TEXT(35)
)

CREATE TABLE mieszkancy(
id INTEGER PRIMARY KEY AUTOINCREMENT,
liczba_mieszkancow INTEGER,
liczba_kobiet INTEGER,
grupa_wiekowa TEXT(20),
data_aktualizacji DATE,
FOREIGN KEY(id_miasta) REFERENCES(miasta)
)

CREATE TABLE powierzchnie(
id INTEGER PRIMARY KEY AUTOINCREMENT,
powierzchnia_miasta DECIMAL,
powierzchnie_zielone INTEGER,
data_aktualizacji DATE,
FOREIGN KEY(id_miasta) REFERENCES(miasta)
)
