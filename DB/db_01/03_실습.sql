-- SQLite
--1.흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.
SELECT smoking, count(smoking)
FROM healthcare
WHERE smoking != ''
GROUP BY smoking;

--2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.
SELECT is_drinking, count(is_drinking)
FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking;

--3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.
SELECT is_drinking, count(blood_pressure)
FROM healthcare
WHERE is_drinking != '' AND blood_pressure>=200
GROUP BY is_drinking;

--4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

SELECT sido, count(sido)
FROM healthcare
GROUP BY sido
HAVING count(sido)>=50000;

--5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.
-- 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.
SELECT height, count(height)
FROM healthcare
GROUP BY height
ORDER BY height
DESC
LIMIT 5;

--6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오.
-- 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.
SELECT weight, height, count(*)
FROM healthcare
GROUP BY weight, height
ORDER BY COUNT(*)
DESC
LIMIT 5;

--7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

SELECT is_drinking, AVG(waist), count(*)
FROM healthcare
WHERE is_drinking!=''
GROUP BY is_drinking
HAVING AVG(waist) AND count(*);

--8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.
--단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

SELECT gender, ROUND(AVG(va_left), 2) AS '평균 왼쪽 시력', ROUND(AVG(va_right), 2) AS '평균 오른쪽 시력'
From healthcare
GROUP BY gender
HAVING va_left AND va_right;

--9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.
-- 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

SELECT age, ROUND(AVG(height), 2) AS '평균 키', ROUND(AVG(weight), 2) AS '평균 몸무게'
From healthcare
GROUP BY age
HAVING AVG(height)>=160 AND AVG(weight)>=60;

--10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

SELECT is_drinking '음주 여부', smoking '흡연 여부', ROUND(AVG(weight/((height*0.01)*(height*0.01))), 2) '평균 BMI'
FROM healthcare
WHERE is_drinking!='' AND smoking!=''
GROUP BY is_drinking, smoking;

--추가 쿼리

SELECT sido, ROUND(MOD(AVG(height), AVG(weight)), 2)
FROM healthcare
GROUP BY sido
HAVING count(sido)>50000;

SELECT sido, POWER(MOD(AVG(height), AVG(weight)), MOD(AVG(height), AVG(weight))) AS '평균키에 평균몸무게를 나눈 값의 제곱'
FROM healthcare
GROUP BY sido
HAVING count(sido)>50000;

SELECT sido, SQRT(POWER(MOD(AVG(height), AVG(weight)), MOD(AVG(height), AVG(weight)))) AS '평균키에 평균몸무게를 나눈 값의 제곱의 제곱근'
FROM healthcare
GROUP BY sido
HAVING count(sido)>50000;