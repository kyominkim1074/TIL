-- SQLite
--a와 b테이블에서 값이 일치하는 것들만 join
SELECT *
FROM users INNER JOIN role
on users.role_id = role.id;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

SELECT
users.name, role.title
FROM users INNER JOIN role
ON users.role_id = role.id;
-- name  title
-- ----  -----
-- 관리자   admin
-- 김철수   staff
-- 이영희   staff

-- 스태프만 출력
SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id
where role.id = 2;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- 이름 내리차순
SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id
ORDER BY users.name DESC;

-- left outer join
SELECT *
FROM articles LEFT OUTER JOIN users
on articles.user_id = users.id;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444

SELECT *
FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id
where articles.user_id IS NOT NULL;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1

SELECT *
FROM articles FULL OUTER JOIN users
on articles.user_id = users.id;

--cross join

SELECT *
FROM users CROSS JOIN role;

-- id  name  role_id  id  title  
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 1   관리자   1        2   staff
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin
-- 2   김철수   2        2   staff
-- 2   김철수   2        3   student
-- 3   이영희   2        1   admin
-- 3   이영희   2        2   staff
-- 3   이영희   2        3   student

-- 3개의 테이블 조인

SELECT *
FROM articles
JOIN users
ON articles.user_id=users.id
JOIN role
ON users.role_id=role.id;

-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin