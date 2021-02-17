-- #1 null 값이 포함된 레코드 조회
-- 동물보호소에 들어온 동물 중, 이름이 없는채로 들어온 동물의 ID를 조회하는 SQL문을 작성해주세요. 단, ID는 오름차순 정렬되어야합니다.
SELECT
  ANIMAL_ID
FROM
  ANIMAL_INS
WHERE
  NAME IS NULL;
-- #2 null 값이 포함되지 않은 레코드 조회
  -- 동물보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL문을 작성해주세요. 단, ID는 오름차순 정렬 되어야합니다.
SELECT
  ANIMAL_ID
FROM
  ANIMAL_INS
WHERE
  NAME IS NOT NULL
ORDER BY
  ANIMAL_ID ASC;
-- #3 null값 대치하기
  -- 입양게시판에 동물정보를 게시하려합니다. 동물의 생물종, 이름, 성별 및 중성화여부를 아이디순으로 조회하는 SQL문을 작성해주세요.
  -- 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 Noname으로 표시해주세요.
SELECT
  ANIMAL_TYPE,
  IFNULL(NAME, 'No name') AS NAME,
  SEX_UPON_INTAKE
FROM
  ANIMAL_INS;