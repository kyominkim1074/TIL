-- SQLite
CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

.mode csv
.import users.csv users



-- 30세 이상인 사람들
SELECT * FROM users WHERE age >= 30;
-- 5명만
SELECT * FROM users WHERE age >= 30 LIMIT 5;
--30이상의 사람의 이름 5명
SELECT first_name FROM users WHERE age >= 30 LIMIT 5;
--30이상 성이 김인 사람들의 이름
SELECT first_name FROM users WHERE age >= 30 AND last_name = '김';

--30세 이상 사람들의 수
SELECT COUNT(*) FROM users WHERE age >= 30;
--가장 최연소의 나이
SELECT MIN(age) FROM users;
--이씨 중에 최연소 나이
SELECT MIN(age) FROM users WHERE last_name = '이';
--이씨 중에 최연소 이름과 계좌잔고
SELECT MIN(age), first_name, balance FROM users WHERE last_name = '이';
--30이상이 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;
--계좌 잔고가 많은 사람
SELECT MAX(balance), first_name FROM users;

-- 지역번호가 02
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
--준으로 끝나는 이름을 가진 사람
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
--중간번호 5114
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';

--나이 오름차순
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
--나이, 성 순으로 오름차순
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
--계좌 잔액 순 내림차순
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
--계좌 잔액 내림차순 성씨 오름차순
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;