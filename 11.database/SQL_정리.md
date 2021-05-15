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





## 1.4. 데이터 분석 단계로 나아가기





## 1.5. 테이블 조인을 통한 깊이있는 데이터 분석





## 1.6. 서브쿼리와 뷰를 활용한 유연한 데이터 분석





# 2. SQL로 하는 데이터 관리





# 3. 데이터베이스 모델링



