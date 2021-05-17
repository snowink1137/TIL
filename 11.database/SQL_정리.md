> 코드잇 개발자를 위한 SQL 데이터베이스 강의 중 다시 볼 내용을 정리한 문서
>
> https://www.codeit.kr/learn/courses/sql-database-for-developers/3136



[TOC]



# 1. SQL로 하는 데이터 분석

## 1.1. 데이터베이스 기본 개념

### 데이터베이스

- 일정한 체계 속에 저장된 데이터의 집합
- 보통 Table 단위로 저장됨



### DBMS

- DataBase Management System
- 사용자는 DBMS를 통해 DATABASE를 사용(조회, 저장 등)한다
- SQL이라는 언어로 DBMS를 조작할 수 있다. 결국 SQL로 DATABASE를 사용하는 것이다
  - SQL은 국제 표준이 있고, DBMS마다 이 표준을 준수하기는 하지만 100%는 아니다. 따라서 DBMS마다 약간씩 다를 수는 있다



### sys 데이터베이스

- 이번 강의에서는 MySQL을 사용하기로 했다. MySQL를 설치하면 기본적으로 sys라는 데이터베이스가 존재한다
- sys 데이터베이스는 MySQL의 성능 관련 정보들을 갖고 있는 데이터베이스이다



## 1.2. 테이블 생성하기

### Primary Key

- 테이블에서 특정 row 하나를 식별하는 역할
- 크게 Natural Key, Surrogate Key 두 개로 구분된다
  - Natural Key
    - 실제로 어떤 개체가 갖고 있는 속성을 Primary Key로 정하는 것
      ex) 주민등록번호, ISBN
  - Surrogate Key
    - Primary Key로 만들기 위해 인위적으로 컬럼을 새로 만들어서 쓰는 것
  - 상황마다 선택해서 쓰는데, 정답은 없다



## 1.3. 데이터 조회로 기본 다지기

### 조건식 예시

```sql
-- 예시 데이터 create query

CREATE TABLE `member` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` text,
  `age` int DEFAULT NULL,
  `gender` text,
  `height` double DEFAULT NULL,
  `weight` double DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `sign_up_day` date DEFAULT NULL,
  `address` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `member` (`id`, `email`, `age`, `gender`, `height`, `weight`, `birthday`, `sign_up_day`, `address`) VALUES 
(1,'codeit@naver.com',28,'m',178.2,70,'1992-01-03','2019-03-26','서울특별시 중구 삼일대로 343 103호'),
(2,'korin02@google.com',29,'m',165.7,67.3,'1992-08-13','2019-02-27','서울특별시 중구 세종대로 110 502호'),
(3,'cowboy@codeit.kr',31,'m',NULL,70.2,'1990-01-03','2019-01-05','경기도 고양시 일산서구 고양대로 633 204동 203호'),
(4,'get_flower@naver.com',-10,'f',183.5,72,'1975-03-12','2018-11-29',NULL),
(5,'taehos@hanmail.net',27,'m',181.3,70,'1992-09-02','2017-03-14','제주 제주시 문연로 6 102동 1105호'),(6,'iamstylish@naver.com',300,'f',172.2,NULL,'1989-01-03','2012-11-15','안드로메다 128행성'),(7,'captainGoGo03@koreauniv.com',28,'m',195.2,66,'1992-03-13','2014-03-18','전라남도 순천시 왕지3길 60 112동 107호'),(8,'sungsos@naver.com',36,'f',167.7,66.2,'1992-01-03','2017-03-20','경기도 부천시 평천로 679 101동 101호'),(9,'young05@naver.com',30,'m',180.2,70.4,'1991-02-13','2013-08-12','경기 오산시 세마문학로 50 111동 109호'),(10,'codeman_to@yonseit.com',111,'f',NULL,70.5,'1970-08-01','2017-02-20','경기 고양시 덕양구 충장로 118 112동 1103호'),(11,'programmer007@sumsung.com',27,'m',170.4,65.3,'1993-03-26','2014-01-22','경기 성남시 수정구 시민로 209 101동 1201호'),(12,'lovely_day@kaisty.com',-10,'f',162.7,69.4,'1995-10-11','2017-07-01','경기 화성시 봉담읍 동화새터길 55-39 203동 205호'),(13,'teddy@kakaot.com',41,'f',177.3,77.2,'1980-11-12','2016-08-03','인천 부평구 아트센터로 118 302동 602호'),(14,'pooh_man@naver.com',28,'m',182,NULL,'1993-12-21','2018-09-02','인천 미추홀구 송림로 194 602동 303호'),(15,'bicycle_go123@yahoot.com',24,'m',180,60.3,'1997-03-03','2019-12-01','서울 송파구 올림픽로 435 103동 501호'),(16,'all_round321@naver.com',26,'m',182.4,NULL,'1995-01-03','2019-11-23',NULL),(17,'nice_man@google.com',200,'m',180.8,NULL,'2003-01-03','2015-10-25','강원도 원주시 가곡로 50 101동 810호'),(18,'jw101@hanmail.net',0,'m',160.3,70,'1992-08-03','2017-09-23','강원도 춘천시 지석로 29 402동 321호'),(19,'cat_movie@lotte.com',-5,'f',180.2,NULL,'1989-01-03','2018-11-25','서울 양천구 오목로 354 110동 402호'),(20,'gogo_shopping@naver.com',32,'m',180.2,80.3,'1989-11-02','2015-01-23','서울 송파구 올림픽로35길 10 파크리오 301동 703호'),(21,'hello_hat@unista.com',26,'f',165.3,48.2,'1995-11-13','2018-12-23',NULL),(22,'new_coder@naver.com',-2,'f',180.7,70,'1976-08-03','2018-12-12','부산 연제구 양연로27번길 26 301동 701호'),(23,'zerotohundred@naver.com',20,'m',162,56,'2001-02-17','2015-07-20',NULL),(24,'xMan_series@naver.com',29,'m',173,65,'1992-01-03','2011-12-20','어린왕자에 나오는 B612');
```



```sql
SELECT * FROM copang_main.member WHERE age >= 27;
SELECT * FROM copang_main.member WHERE age BETWEEN 30 AND 39;
SELECT * FROM copang_main.member WHERE age NOT BETWEEN 30 AND 39;
SELECT * FROM copang_main.member WHERE gender != 'm';
SELECT * FROM copang_main.member WHERE gender <> 'm';

-- date 타입도 부등호, BETWEEN 사용 가능
SELECT * FROM copang_main.member WHERE sign_up_day > '2019-01-01';
SELECT * FROM copang_main.member WHERE sign_up_day BETWEEN '2018-01-01' AND '2018-12-31';

-- 문자열 패턴 매칭 조건 LIKE
SELECT * FROM copang_main.member WHERE address LIKE '서울%'  -- '서울'로 시작하는 임의의 길이 단어
SELECT * FROM copang_main.member WHERE email LIKE 'c______@%'  -- 'c'로 시작하고 뒤에 임의의 6글자가 있고 @가 나온 이후, 임의의 길이 단어를 검색
SELECT * FROM copang_main.test WHERE sentence LIKE BINARY '%g%'  -- BINARY 붙이면 utf8mb4_0900_ai_ci charset에서도 대소문자 구분 가능. ci <==> case-insensitive

SELECT * FROM copang_main.member WHERE age IN (20, 30);  -- 20이거나 30이어야 함
```



### DATE 타입 관련 함수 예시

```sql
SELECT * FROM copang_main.member WHERE YEAR(birthday) = '1992';
SELECT * FROM copang_main.member WHERE MONTH(sign_up_day) IN (6, 7, 8);
SELECT * FROM copang_main.member WHERE DAYOFMONTH(sign_up_day) BETWEEN 15 AND 31;

SELECT email, sign_up_day, DATEDIFF(sign_up_day, '2019-01-01') FROM copang_main.member;  -- 기준 날짜에서 며칠 차이 나는지 확인하는 함수
SELECT email, sign_up_day, CURDATE() DATEDIFF(sign_up_day, CURDATE()) FROM copang_main.member;  -- CURDATE(): 오늘 날짜 구하는 함수

SELECT email, sign_up_day, DATE_ADD(sign_up_day, INTERVAL 300 DAY) FROM copang_main.member;
SELECT email, sign_up_day, DATE_SUB(sign_up_day, INTERVAL 250 DAY) FROM copang_main.member;

SELECT email, sign_up_day, UNIX_TIMESTAMP(sign_up_day) FROM copang_main.member;
SELECT email, sign_up_day, FROM_UNIX_TIMESTAMP(UNIX_TIMESTAMP(sign_up_day)) FROM copang_main.member;
```



### AND, OR

- `WHERE id = 1 OR id = 2` 이렇게 다 적어줘야 한다. `WHERE id = 1 OR 2` 이렇게 적으면, `WHERE id = 1 OR TRUE` 이렇게 인식됨
- AND와 OR를 나란히 쓰면 AND가 우선 적용된다. 괄호를 씌우던가 순서를 잘 정의해야 한다



### 정렬(ORDER BY)

```sql
SELECT * FROM copang_main.member ORDER BY YEAR(sign_up_day) DESC, email ASC;  -- 앞 쪽에 적힌 기준으로 먼저 정렬한 후 그 다음 기준으로 정렬한다

SELECT * FROM FOR_TEST.ordering_test ORDER BY data ASC; -- data가 숫자형(int, double)인지 문자형(text)인지에 따라 정렬 방법이 다르다
/*
숫자형 일때는 19 27 120 230 으로 정렬되지만,
문자형 일때는 120 19 230 27 순으로 정렬된다.

아래처럼 하면 문자형 data여도 숫자형처럼 정렬할 수 있다
*/
SELECT * FROM FOR_TEST.ordering_test ORDER BY CAST(data AS signed) ASC;
SELECT * FROM FOR_TEST.ordering_test ORDER BY CAST(data AS decimal) ASC;

SELECT * FROM FOR_TEST.ordering_test ORDER BY CAST(data AS CHAR) ASC;  -- 반대로 이렇게 쓰면 숫자형 data를 문자 정렬하듯이 할 수 있다
```



### SQL 절 순서 문법

- https://dev.mysql.com/doc/refman/8.0/en/select.html



### 데이터 일부만 추려보기(LIMIT)

```sql
SELECT * FROM copang_main.member
ORDER BY sign_up_day DESC
LIMIT 10;  -- 앞에서부터 10개만 추려보기

SELECT * FROM copang_main.member
ORDER BY sign_up_day DESC
LIMIT 8, 2;  -- 9번째(index가 0부터 시작함)부터 2개만 추려보기


-- 두 번째 방식(LIMIT m, n)을 응용해서 pagination을 구현한다. 실무에서는 이렇게 간단하지는 않고 다양한 기법이 추가된다고 한다
SELECT * FROM db.search_result ~ ORDER BY registration_date DESC LIMIT 0, 10  -- 1페이지

SELECT * FROM db.search_result ~ ORDER BY registration_date DESC LIMIT 10, 10  -- 2페이지

SELECT * FROM db.search_result ~ ORDER BY registration_date DESC LIMIT 20, 10  -- 3페이지

SELECT * FROM db.search_result ~ ORDER BY registration_date DESC LIMIT 30, 10  -- 4페이지
```



## 1.4. 데이터 분석 단계로 나아가기

### 집계 함수(Aggregate Function)

- 특정 컬럼의 여러 row의 값들을 동시에 고려해서 실행되는 함수
- COUNT, MAX, MIN, AVG, SUM, STD 등
- NULL은 빼고 계산해준다



### 산술 함수(Mathematical Function)

- 특정 컬럼의 각 row의 값마다 실행되는 함수
- ABS, SQRT, CEIL(올림 함수), FLOOR, ROUND 등
  - https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html



### NULL

```sql
-- NULL을 다른 문자로 바꿔서 조회하기
SELECT
	COALESCE(height, '###')  -- height가 NULL이면 ###을 출력해줌
	COALESCE(weight, '---')
	COALESCE(address, '@@@')
FROM copang_main.member;

SELECT * FROM copang_main.member WHERE address IS NULL;
SELECT * FROM copang_main.member WHERE address = NULL;  -- 이렇게 쓰면 안됨! NULL은 그냥 없는 거니까 등호로 비교할 수 있는 대상이 아님

SELECT *, height+3 FROM copang_main.member;  -- NULL인 경우 어떤 연산을 해도 그냥 NULL이다
```



### 컬럼 값 변환하여 보기

```sql
-- 단순 CASE 함수
SELECT email,
CASE age  -- 비교 대상이 먼저 나옴!
	WHEN 29 THEN '스물 아홉 살'
	WHEN 30 THEN '서른 살'
	ELSE age
END
FROM copang_main.member;

-- 검색 CASE 함수(비교 대상이 먼저 나오지 않는다)
SELECT
	email,
	CONCAT(height, 'cm', ', ', weight, 'kg') AS '키와 몸무게',  -- CONCAT(): 문자열 잇는 함수
	weight / ((height/100) * (height/100)) AS BMI,
CASE
	WHEN weight IS NULL OR height is NULL THEN '비만 여부 알 수 없음'
	WHEN weight / ((height/100) * (height/100)) >= 25 THEN '과체중 또는 비만'
	WHEN weight / ((height/100) * (height/100)) >= 18.5
		AND WHEN weight / ((height/100) * (height/100)) < 25
		THEN '정상'
	ELSE '저체중'
END
FROM copang_main.member;
```



### NULL 처리 함수 정리

- COALESCE
  - COALESCE(column, 'NULL대체표현')
  - COALESCE(column, 'NULL대체표현1', 'NULL대체표현2')
    - ex) COALESCE(height, weight * 2.3, 'N/A')
- IFNULL
  - MySQL에만 있는 함수. 파라미터 2개만 가능
  - IFNULL(column, 'NULL대체표현')
- IF
  - IF(조건문, 'true인 경우 리턴 값', 'false인 경우 리턴 값')
  - ex) IF(height IS NOT NULL, height, 'N/A')
- CASE ~ END
  - ex)
    CASE
        WHEN height IS NOT NULL THEN height
        ELSE 'N/A'
    END



### 고유 값만 보기

```sql
SELECT DISTINCT(SUBSTRING(address, 1, 2))  -- address 컬럼의 1번째 자리부터 2개 문자를 추출해서 고유값 조회 ex) 서울, 경기
FROM copang_main.member;
```



### 문자열 관련 함수들

- LENGTH
  - 문자열 길이 구해줌
- UPPER, LOWER
  - 모두 대문자 or 모두 소문자로 바꿔줌
- LPAD, RPAD
  - 왼쪽 or 오른쪽에 특정 문자를 채운다(PADDING)
  - ex) LPAD(age, 10, '0') : 총 10자리를 쓸건데 모자라면 왼쪽에 문자 '0'을 붙인다
- LTRIM, RTRIM
  - 왼쪽 or 오른쪽 공백 삭제
- TRIM
  - 양쪽 공백 삭제



### 그루핑해서 보기

- GROUP BY 절은 특정 컬럼을 대상으로 ROW들을 그룹지어 준다
  - 그냥 SELECT 하면 DISTINCT와 다를 바 없어보이지만, 집계 함수를 사용할 때는 다르다. 집계 함수의 대상이 각 GROUP이 되어서 여러 개의 결과가 나올 수 있다

![image-20210517185707050](SQL_정리.assets/image-20210517185707050.png)







## 1.5. 테이블 조인을 통한 깊이있는 데이터 분석





## 1.6. 서브쿼리와 뷰를 활용한 유연한 데이터 분석





# 2. SQL로 하는 데이터 관리





# 3. 데이터베이스 모델링



