# 20190415 django ORM

## 수업

### django-extensions 모듈의 shell_plus를 jupyter notebook에서 쓰기

- 설치: `$ pip install "ipython[notebook]"`
- 실행: `$ python manage.py shell_plus --notebook`



### 존재하는 DB 새로 초기화하기

- 특정 App과 관련된 모든 DB 테이블을 Drop한다.
  - ` $ python manage.py migrate [APP_NAME] zero`
- 해당 App의 `migrations/`안의 마이그레이션 파일을 삭제한다.
  - `$ rm [APP_NAME]/migrations/0*`
- 다시 마이그레이션 파일을 만든다.
  - `$ python manage.py makemigrations [APP_NAME]`
- 다시 마이그레이트!
  - `$ python manage.py migrate [APP_NAME]`



### One To One model

#### User

| id      | email       | password  |
| ------- | ----------- | --------- |
| PK, INT | CharField   | CharField |
| 1       | neo@hphk.kr | 123123    |

#### Profile

| id      | user_id       | first_name | last_name |
| ------- | ------------- | ---------- | --------- |
| PK, INT | FK, User, INT | CharField  | CharField |
| 1       | 1             | TaeYoung   | Yu        |



### One To Many model

#### Writer

| id (PK) | name      |
| ------- | --------- |
| INT     | CharField |

#### Book

| id (PK) | author_id (FK - Writer) | title     | description |
| ------- | ----------------------- | --------- | ----------- |
| INT     | INT                     | Charfield | TextField   |

#### Chapter

| id (PK) | book_id (FK - Book) | title     | description |
| ------- | ------------------- | --------- | ----------- |
| INT     | INT                 | CharField | TextField   |







## 수업 외

