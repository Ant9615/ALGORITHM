-- #1 모든 레코드 조회
-- 동물 보호소에 들어온 모든 동물의 정보를
-- ANIMAL_ID 순으로 조회
SELECT
  *
FROM
  ANIMAL_INS;
-- #2 역순 정렬
  -- 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
  -- 이때 결과는 ANIMAL_ID 역순으로 보여주세요.
SELECT
  NAME,
  DATETIME
FROM
  ANIMAL_INS
ORDER BY
  ANIMAL_ID DESC;
-- #3 특정 속성값 포함된 레코드 찾기1
  -- 동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
  -- 이때 결과는 아이디순으로 조회해주세요.
SELECT
  ANIMAL_ID,
  NAME
FROM
  ANIMAL_INS
WHERE
  INTAKE_CONDITION = 'Sick';
-- #4 특정 속성값 포함된 레코드 찾기2
  -- 동물 보호소에 들어온 동물 중 젊은 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
  -- 이때 결과는 아이디순으로 조회해주세요.
SELECT
  ANIMAL_ID,
  NAME
FROM
  ANIMAL_INS
WHERE
  INTAKE_CONDITION != 'Aged';
-- #5 정렬
  -- 동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.
  -- SQL을 실행하면 다음과 같이 출력되어 야합니다.
SELECT
  ANIMAL_ID,
  NAME
FROM
  ANIMAL_INS
ORDER BY
  ANIMAL_ID;
-- #6 여러 기준으로 정렬
  -- 동물 보호소에 들어온 모든 동물의 아이디와 이름,
  -- 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요.
  -- 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
SELECT
  ANIMAL_ID,
  NAME,
  DATETIME
FROM
  ANIMAL_INS
ORDER BY
  NAME ASC,
  DATETIME DESC;
-- #7 상위 n개 레코드
  -- 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL문을 작성해주세요.
SELECT
  NAME
FROM
  ANIMAL_INS
ORDER BY
  DATETIME ASC
LIMIT
  1;