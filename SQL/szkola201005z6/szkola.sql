DROP TABLE IF EXISTS uczniowie;

CREATE TABLE uczniowie(
id_ucznia INTEGER PRIMARY KEY,
nazwisko TEXT,
imie TEXT,
ulica TEXT,
dom INTEGER,
id_klasy TEXT
);

DROP TABLE IF EXISTS przedmioty;

CREATE TABLE przedmioty(
id_przedmiotu INTEGER PRIMARY KEY,
nazwa_przedmiotu TEXT,
nazwisko_naucz TEXT,
imie_naucz TEXT
);

DROP TABLE IF EXISTS oceny;

CREATE TABLE oceny(
ocena INTEGER,
id_ucznia INTEGER,
id_przedmiotu INTEGER,
dataa DATE,
FOREIGN KEY (id_ucznia) REFERENCES uczniowie(id_ucznia),
FOREIGN KEY (id_przedmiotu) REFERENCES przedmioty(id_przedmiotu)
);
