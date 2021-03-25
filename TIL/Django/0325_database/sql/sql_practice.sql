-- 한줄 주석
/*
여러줄 주석
*/


/*
SELECT 구문 순서

SELECT 컬럼 목록
FROM 테이블명
WHERE 로우 필터링 조건
ORDER BY 컬럼
LIMIT 카운트 OFFSET 카운트
GROUP BY 컬럼
HAVING 그룹 필터링 조건;

*/


-- SELECT
SELECT * FROM examples;

-- CREATE TABLE
CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,
  name TEXT 
);

-- DROP TABLE
-- (주.의.)
-- 이 명령어를 치기 전에는 반드시 3번 이상 스스로에게
-- 내가 이 명령어를 쳐도 되는지 되묻습니다.
DROP TABLE classmates;

CREATE TABLE classmates(
  name TEXT,
  age INT,
  address TEXT
);

INSERT INTO classmates(
  name,age,address)
  VALUES('홍길동',30,'서울');

-- SELECT (rowid)
SELECT rowid, *FROM classmates;
-- SQL이 자동으로 만들어주는 PK 필드

-- CREATE TABLEwith NOT NULL
-- 주의 ! PK는 INTEGER 만 사용 가능하다.
DROP TABLE classmates;
CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

-- INSERT (errors)
INSERT INTO classmates (name,age)
VALUES ('홍길동',23);
-- NOT NULL 에러가 뜬다. <-- Django에서 봤던거 

INSERT INTO classmates -- 그리고 항상 컬럼까지 지정해줘라 안쓰면 전체 column을 설정하긴 하는데
VALUES ('홍길동',23,'서울'); 

--INSERT (correct)
INSERT INTO classmates(name,age,address)
VALUES ('홍길동',23,'서울');

-- CREATE TABLE (without id)
DROP TABLE classmates;
CREATE TABLE classmates(
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates (name,age,address)
VALUES ('용재',19,'광주');

-- SELECT with LIMIT
SELECT rowid,name 
FROM classmates
LIMIT 1;

SELECT rowid,name
FROM classmates
LIMIT 1 OFFSET 2;

-- SELECT with WHERE clause

SELECT * FROM classmates WHERE address='광주';

-- SELECT with DISTINCT <-- age값 전체를 중복 없이 가져온다.
SELECT DISTINCT age
FROM classmates;

-- DELETE
-- 반드시 SELECT로 먼저 정확한 값이 갖고 와지는지 확인 후 지웁니다.
DELETE FROM classmates
WHERE rowid=4;

--AVG
-- 30살 이상인 사람들의 평균 나이
SELECT AVG(age)
FROM users
WHERE age >= 30;

--MAX
SELECT first_name, MAX(balance)
FROM users;


SELECT phone, AVG(balance)
FROM users
WHERE age >=30


-- WHERE with WILDCARD

SELECT first_name, age
FROM users
WHERE age LIKE('2_');

--ORDER BY
SELECT age
FROM users
ORDER BY age
LIMIT 10; -- 10개 한정으로 뽑는다.

SELECT age, last_name
FROM users
ORDER BY age, last_name
LIMIT 10;

SELECT last_name, first_name,balance
FROM users
ORDER BY balance DESC
LIMIT 10;

-- GROUP BY
SELECT last_name,count(*)
FROM users
GROUP BY last_name;


SELECT last_name,first_name,count(*)
FROM users
GROUP BY last_name,first_name; --first_name과 last_name을 하나의 데이터로 묶은 다음에 그 자체를 1개로 count


--ALTER
CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
  );


INSERT INTO articles(title,content)
VALUES('1번 제목','1번 내용');

ALTER TABLE articles
RENAME TO news;

ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;

--JOIN...까지 알아봐라 SQL 공부!