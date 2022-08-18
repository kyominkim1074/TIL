-- SQLite

--성별 개수
SELECT  last_name, COUNT(*)
FROM users
GROUP BY last_name;

SELECT  last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name, age
FROM users
WHERE last_name = '곽';

SELECT *
FROM users
LIMIT 5;

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;

---오류
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name)>100
GROUP BY last_name;
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name)>100 GROUP B
--                                       error here ---^


--HAVING을 쓴 경우
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name)>100;
-- last_name  COUNT(last_name)
-- ---------  ----------------
-- 김          268
-- 이          179