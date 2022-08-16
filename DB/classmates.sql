-- SQLite
CREATE TABLE classmates(
name TEXT,
age INTEGER,
address TEXT
);

INSERT INTO classmates (name, age) VALUES ('심영', 23);
SELECT * FROM classmates;
INSERT INTO classmates (name, age, address) VALUES ('심영', 23, '서울');
INSERT INTO classmates VALUES ('김두한', 40, '서울');

SELECT rowid, * FROM classmates;
DROP TABLE classmates;