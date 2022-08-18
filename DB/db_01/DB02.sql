-- SQLite

--1.
SELECT COUNT(*) FROM healthcare;
--COUNT(*)
--------
--1000000

--2.
SELECT MIN(age), MAX(age) FROM healthcare;
-- MIN(age)  MAX(age)
-- --------  --------
-- 9         18

--3.
SELECT MIN(height),MIN(weight), MAX(height), MAX(weight) FROM healthcare;
-- MIN(height)  MIN(weight)  MAX(height)  MAX(weight)
-- -----------  -----------  -----------  -----------
-- 130          30           195          135

--4.
SELECT COUNT(*) FROM healthcare WHERE height>=160 AND height<=170;
-- COUNT(*)
-- --------
-- 516930

--5.
SELECT * FROM healthcare WHERE is_drinking=1 AND waist !='' ORDER BY waist DESC LIMIT 5;
SELECT * FROM healthcare WHERE is_drinking=1 AND waist <>'' ORDER BY waist DESC LIMIT 5;
-- id      sido  gender  age  height  weight  waist  va_left  va_right  blood_pressure  smoking  is_drinking       
-- ------  ----  ------  ---  ------  ------  -----  -------  --------  --------------  -------  -----------       
-- 993531  48    1       9    170     130     146.0  0.6      0.8       150             3        1
-- 87897   48    1       10   170     130     142.0  0.6      0.8       140             1        1
-- 826643  48    1       9    180     135     141.4  1.2      0.9       136             3        1
-- 567314  26    1       11   170     110     140.0  0.3      0.6       125             3        1
-- 611146  36    1       12   165     120     140.0  0.4      0.8       141             3        1

--6.
SELECT COUNT(*) FROM healthcare WHERE va_left>=1.5 AND va_right>=1.5 AND is_drinking=1;
-- COUNT(*)
-- --------
-- 36697

--7.
SELECT COUNT(*) FROM healthcare WHERE blood_pressure<120;
-- COUNT(*)
-- --------
-- 360808

--8.
SELECT AVG(waist) FROM healthcare WHERE blood_pressure>=140;
-- AVG(waist)
-- ----------------
-- 85.8665098512525

--9.
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender=1;
-- AVG(height)       AVG(weight)
-- ----------------  ----------------
-- 167.452735422145  69.7131620222875

--10.
SELECT height, weight FROM healthcare ORDER BY height DESC LIMIT 1 OFFSET 2;
-- height  weight
-- ------  ------
-- 195     85

--11.
SELECT COUNT(*) FROM healthcare WHERE (weight/((height*height)*0.0001))>=30;
SELECT COUNT(*) FROM healthcare WHERE weight/((height*0.01)*(height*0.01))>=30;
-- COUNT(*)
-- --------
-- 53121

--12.
SELECT id, weight/((height*height)*0.0001) AS BMI FROM healthcare WHERE smoking=3 ORDER BY (weight/((height*height)*0.0001)) DESC LIMIT 5;
-- id      weight/((height*height)*0.0001)
-- ------  -------------------------------
-- 231431  50.78125
-- 934714  49.9479708636837
-- 722707  48.828125
-- 947281  47.7502295684114
-- 948801  47.7502295684114

--13.혈압 140이상의 사람의 수를 구하기
SELECT COUNT(*) FROM healthcare WHERE blood_pressure>=140;
-- COUNT(*)
-- --------
-- 145819

--14. 흡연3, 음주 1인 사람들의 키와 몸무게 평균 구하기
SELECT AVG(height), AVG(weight) FROM healthcare WHERE smoking=3 AND is_drinking;
-- AVG(height)      AVG(weight)
-- ---------------  ----------------
-- 167.69321832124  69.4941839971801

--15. 흡연자(3)와 음주하는 사람(1)의 몸무게를 내림차순을 5명
SELECT * FROM healthcare WHERE is_drinking=1 AND smoking=3 AND weight !='' ORDER BY weight DESC LIMIT 5;