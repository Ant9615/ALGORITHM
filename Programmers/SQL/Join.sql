-- #1 left join
-- 천재지변으로 인해 일부데이터가 유실되었습니다. 입양을 간 기록은 있는데,
-- 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID순으로 조회하는 SQL문을 작성해주세요.
SELECT
  ANIMAL_OUTS.ANIMAL_ID,
  ANIMAL_OUTS.NAME
FROM
  ANIMAL_OUTS
  LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE
  ANIMAL_INS.ANIMAL_ID IS NULL
ORDER BY
  ANIMAL_OUTS.ANIMAL_ID ASC;
-- #2 exclusive join
  -- 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호시작일보다 입양일이 더 빠른동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
  -- 이때 결과는 보호시작일이 빠른순으로 조회해야합니다.
SELECT
  ANIMAL_OUTS.ANIMAL_ID AS NAME,
  ANIMAL_OUTS.NAME
FROM
  ANIMAL_OUTS
  LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE
  ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY
  ANIMAL_INS.DATETIME ASC;
-- #3 exclusive join 2
  -- 아직 입양을 못간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
  -- 이때 결과는 보호시작일 순으로 조회해야합니다.
SELECT
  ANIMAL_INS.NAME AS NAME,
  ANIMAL_INS.DATETIME
FROM
  ANIMAL_INS
  LEFT JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE
  ANIMAL_OUTS.ANIMAL_ID IS NULL
ORDER BY
  ANIMAL_INS.DATETIME ASC
LIMIT
  3;
-- #4 exclusive join 4
  -- 보호소에서 중성화수술을 거친 동물정보를 알아보려합니다. 보호소에 들어올 당시에는 중성화 되지않았지만,
  -- 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물종, 이름을 조회하는 아이디순으로 조회하는 SQL문을 작성해주세요.
SELECT
  ANIMAL_INS.ANIMAL_ID,
  ANIMAL_INS.ANIMAL_TYPE,
  ANIMAL_INS.NAME
FROM
  ANIMAL_INS
  LEFT JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE
  ANIMAL_INS.SEX_UPON_INTAKE != ANIMAL_OUTS.SEX_UPON_OUTCOME
ORDER BY
  ANIMAL_OUTS.ANIMAL_ID ASC;