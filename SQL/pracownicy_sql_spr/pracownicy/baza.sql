DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie VARCHAR(30),
    nazwisko VARCHAR(30),
    kod TEXT,
    miasto_z TEXT,
    ulica TEXT,
    data_ur DATE,
    miasto_u TEXT
);

DROP TABLE IF EXISTS place;
CREATE TABLE place(
    id_p INTEGER NOT NULL,
    id_s INTEGER,
    placa INTEGER,
    data_z DATE,
    
    FOREIGN KEY(id_p) REFERENCES pracownicy(id),
    FOREIGN KEY(id_s) REFERENCES stanowiska(id_s)
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska(
id_s INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT
);

DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty(
    id_pracownika INTEGER NOT NULL,
    typ_k TEXT,
    kontakt TEXT,
    uwagi TEXT,
    
    FOREIGN KEY(id_pracownika) REFERENCES pracownicy(id)
);
