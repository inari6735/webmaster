DROP TABLE IF EXISTS tbUczniowie;
DROP TABLE IF EXISTS tbKlasy;

CREATE TABLE tbUczniowie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
	id_klasa INTEGER,
	egzHum NUMERIC NOT NULL DEFAULT 0, /*gdy nie uzyska informacji zamienia wartość w polu na 0*/
	egzMat NUMERIC NOT NULL DEFAULT 0, /*gdy nie uzyska informacji zamienia wartość w polu na 0*/
	egzJet NUMERIC NOT NULL DEFAULT 0, /*gdy nie uzyska informacji zamienia wartość w polu na 0*/
	FOREIGN KEY (id_klasa) REFERENCES tbKlasy(id)
);

CREATE TABLE tbKlasy
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	klasa TEXT,
	rokNaboru INTEGER,
	rokMatury INTEGER
);

INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017, 2020);
INSERT INTO tbKlasy VALUES (NULL, '2A', 2016, 2019);
INSERT INTO tbKlasy VALUES (NULL, '1C', 2017, 2020);

INSERT INTO tbUczniowie (id, nazwisko, plec, id_klasa, egzHum, egzMat, egzJez) /*dodawanie danych*/
VALUES (NULL, 'Adam', 'Słodowy', 0, 3, 70.5, 80, 90);

UPDATE tbUczniowie SET egzJez = 100 WHERE id = 1;