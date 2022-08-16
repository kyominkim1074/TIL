-- SQLite
--1.
SELECT COUNT(*) FROM healthcare;

--2.
SELECT * FROM healthcare WHERE age < 10;

--3.
SELECT * FROM healthcare WHERE gender=1;

--4.
SELECT * FROM healthcare WHERE smoking=3 AND is_drinking=1;

--5.
SELECT * FROM healthcare WHERE va_left>=2.0 and va_right>=2.0;

--6.
SELECT DISTINCT sido FROM healthcare;