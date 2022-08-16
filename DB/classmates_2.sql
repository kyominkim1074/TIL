-- SQLite
CREATE TABLE classmates(
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('심영', 30, '서울'),
('김두한', 26, '서울'),
('이정재', 29, '서울'),
('상하이조', 28, '서울');

SELECT * FROM classmates;

SELECT rowid, name FROM classmates;

-- id가 n번째 까지만 출력
SELECT rowid, name FROM classmates LIMIT 2;

-- n번째 까지, id n개 건너뛰어서(?) 출력
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

--주소가 서울인 경우의 데이터를 조회
SELECT * FROM classmates WHERE address='서울';

--나이가 30이상인 데이터를 조회
SELECT * FROM classmates WHERE age >= 30;

--특정 데이터를 중복없이 조회
SELECT DISTINCT age FROM classmates;

SELECT DISTINCT address FROM classmates;

--삭제
DELETE FROM classmates WHERE rowid=5;

INSERT INTO classmates VALUES ('벌처', 40, '대전');
SELECT rowid, * FROM classmates;

--수정
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
SELECT rowid, * FROM classmates;

DROP TABLE classmates;