-- SQLite
CREATE TABLE members(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);

INSERT INTO members VALUES
(1, '홍길동'),
(2, '김철수'),
(3, '심영'),
(4, '김두한'),
(5, '이정재');

DELETE FROM members WHERE rowid=5;
INSERT INTO members (name) VALUES ('상하이');
SELECT * FROM members;

DROP TABLE members;