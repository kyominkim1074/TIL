-- SQLite

CREATE TABLE classmates (
id INTEGRE PRIMARY KEY,
name TEXT NOT NULL,
age INTEGRE NOT NULL,
address TEXT
);

INSERT INTO classmates(id, name, age,  address)
VALUES (1, '홍익', 20, 'kor');
INSERT INTO classmates(id, name, age,  address)
VALUES (2, '동양', 19, 'kor');
INSERT INTO classmates(id, name, age,  address)
VALUES (3, '해양', 23, 'kor');
INSERT INTO classmates(id, name, age,  address)
VALUES (4, '해태', 33, 'kor');
INSERT INTO classmates(id, name, age,  address)
VALUES (5, '로진', 54, 'kor');