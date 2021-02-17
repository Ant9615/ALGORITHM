-- #1 조건에 맞는 counting
-- 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇마리인지 조회하는 SQL문을 작성해주세요
-- 이때 고양이를 개보다 먼저 조회해주세요.
SELECT
  ANIMAL_TYPE,
  COUNT(ANIMAL_TYPE) AS count
FROM
  ANIMAL_INS
GROUP BY
  ANIMAL_TYPE
ORDER BY
  count ASC;
-- #2 같은 조건 counting
  -- 동물 보호소에 들어온 동물이름중 두번 이상 쓰인 이름과 해당이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요.
  -- 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름순으로 조회해주세요.
SELECT
  NAME,
  COUNT(NAME) AS count
FROM
  ANIMAL_INS
WHERE
  NAME IS NOT NULL
GROUP BY
  NAME
HAVING
  COUNT(NAME) >= 2
ORDER BY
  NAME ASC;
-- #3 시각 구하기 1
  --  보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려합니다.
  -- 09:00부터 19:59까지, 각 시간대별로 입양이 몇건이나 발생했는지 조회하는 SQL문을 작성해주세요.
  -- 이때 결과는 시간대 순으로 정렬해야합니다.
SELECT
  HOUR(DATETIME) AS HOUR,
  COUNT(HOUR(DATETIME))
FROM
  ANIMAL_OUTS
WHERE
  HOUR(DATETIME) BETWEEN 9
  AND 20
GROUP BY
  HOUR(DATETIME)
ORDER BY
  HOUR(DATETIME) ASC;
-- #4 시 각 구 하 기 2