[TOC]

> 코드잇 데이터 사이언스 입문 강의 중 다시 볼 내용을 정리한 문서
>
> https://www.codeit.kr/learn/courses/data-science



# 데이터 사이언스 개요

## 데이터 사이언스

### 데이터 사이언스란?

- 데이터를 다루는 일
- 데이터가 많다 → 할 수 있는 일이 많다
- 데이터를 모으는 일등 공신은 소프트웨어
  - 데이터를 모으고 분석하는 일은 과거에도 있었다
  - 하지만 소프트웨어의 발전과 함께 그 중요성이 증대됨
- 데이터 과학이란, 다양한 데이터로부터 지식과 인사이트를 추출하는 분야다
- 프로그래밍 + 수학/통계 + 도메인 지식



### 데이터 사이언스에 대한 오해

1. 데이터 사이언스에서 가장 중요한 건 인공지능, 딥러닝이다

![image-20201021194403463](data_science_입문_정리.assets/image-20201021194403463.png)

![img](data_science_입문_정리.assets/1_7IMev5xslc9FLxr9hHhpFw.png)

- 인공 지능, 딥러닝이 전부는 아니다. 많은 기업들은 인공지능 아래 단계까지만 해도 적은 노력으로 큰 효과를 거둘 수 있음
- 출처: https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007



2. 데이터 사이언티스트는 하루 종일 수학과 컴퓨터만 하는 사람일 것 같다

- 비즈니스에 필요한 핵심 및 문제점을 파악하기 위해서는 인사이트와 커뮤니케이션도 중요하다. 도메인 지식도 필요하고 다양한 부서의 사람들과 소통해야 하기 때문이다. ex) 마케팅 부서, 엔지니어 부서, 경영 부서 등



### 데이터 사이언스 프로세스

1. 문제 정의하기

   - 목표 설정
   - 기간 설정
   - 평가 방법 설정
   - 필요한 데이터 설정

2. 데이터 모으기

   - 웹 크롤링
   - 자료 모으기
   - 기존에 있는 데이터 파일 읽고 쓰기

3. 데이터 다듬기

   - > garbage in, gabage out

   - 데이터 관찰하기

   - 데이터 오류 제거

   - 데이터 정리하기

4. 데이터 분석하기

   - 데이터 파악하기
   - 데이터 변형하기
   - 통계 분석
   - 인사이트 발견
   - 의미 도출

5. 데이터 시각화 및 커뮤니케이션

   - 다양한 시각화
   - 커뮤니케이션
   - 리포트



## Numpy

- Numerical Python

- numpy array vs python list

  - numpy는 C로 쓰여 있어서 그냥 python으로 계산하는 것보다 빠르다. 따라서 많은 데이터를 다룰 때 성능이 좋다

- 배열 중심으로 계산할 때 표현이 간단하다

- ```python
  # ex1)
  import numpy as np
  
  revenue_in_yen = [
      300000, 340000, 320000, 360000, 
      440000, 140000, 180000, 340000, 
      330000, 290000, 280000, 380000, 
      170000, 140000, 230000, 390000, 
      400000, 350000, 380000, 150000, 
      110000, 240000, 380000, 380000, 
      340000, 420000, 150000, 130000, 
      360000, 320000, 250000
  ]
  
  revenue_in_yen_array = np.array(revenue_in_yen)
  filter = np.where(revenue_in_yen_array <= 200000)
  bad_days_revenue = revenue_in_yen_array[filter]
  
  bad_days_revenue
  ```




## Pandas

- Numpy를 기본적으로 포함하고, 외부 데이터 읽고 쓰기, 데이터 정리, 데이터 분석 등의 기능을 추가한 라이브러리

- Data science에서 Python의 인기가 많아지게 한 라이브러리

- 그럼 Numpy 안쓰고 Pandas만 쓰면 되지 않나?

  - Numpy 만의 장점이 있음. 연산이 빠르다는 점 그리고 선형대수, 푸리에변환 등 산술계산에 필요한 여러 기능이 있음
  - Pandas는 구조화된 데이터들을 변형하거나 자르는 등 유연하게 처리하는 데 특화되어 있음
  - 따라서 두 가지를 함께 쓰는 경우가 많다
  - Numpy: 수학과 과학 연산을 위한 파이썬 패키지.  
    참고: https://medium.com/@5eo1ab/numpy-%EC%93%B0%EB%8A%94-%EC%9D%B4%EC%9C%A0-37895f4fdc03
  - Pandas: 데이터 베이스(데이터 프레임)을 다루기 위한 패키지.  
    참고: https://medium.com/@5eo1ab/pandas-%EC%93%B0%EB%8A%94-%EC%9D%B4%EC%9C%A0-9063a90b0bd5

- ```python
  # ex1)
  import pandas as pd
  
  celebrities = [
      ['Taylor Swift', 'December 13, 1989', 'Singer-songwriter'],
      ['Aaron Sorkin', 'June 9, 1961', 'Screenwriter'],
      ['Harry Potter', 'July 31, 1980', 'Wizard'],
      ['Ji-Sung Park', 'February 25, 1981', 'Footballer']
  ]
  
  df = pd.DataFrame(celebrities, columns=['name', 'birthday', 'occupation'])
  
  # ex2) ⇔ ex1)
  dict1 = {
      'name': ['Taylor Swift', 'Aaron Sorkin', 'Harry Potter', 'Ji-Sung Park'],
      'birthday': ['December 13, 1989', 'June 9, 1961', 'July 31, 1980', 'February 25, 1981'],
      'occupation': ['Singer-songwriter', 'Screenwriter', 'Wizard', 'Footballer'],
  }
  df = pd.DataFrame(dict1)
  ```



# DataFrame 다루기

## DataFrame 인덱싱

| 이름으로 인덱싱하기           | 기본 형태                             | 단축 형태                      |
| ----------------------------- | ------------------------------------- | ------------------------------ |
| 하나의 row 이름               | `df.loc["row4"]`                      |                                |
| row 이름의 리스트             | `df.loc[["row4", "row5", "row3"]]`    |                                |
| row 이름의 리스트 슬라이싱    | `df.loc["row2":"row5"]`               | `df["row2":"row5"]`            |
| 하나의 column 이름            | `df.loc[:, "col1"]`                   | `df["col1"]`                   |
| column 이름의 리스트          | `df.loc[:, ["col4", "col6", "col3"]]` | `df[["col4", "col6", "col3"]]` |
| column 이름의 리스트 슬라이싱 | `df.loc[:, "col2":"col5"]             |                                |

| 위치로 인덱싱하기             | 기본 형태               | 단축 형태 |
| ----------------------------- | ----------------------- | --------- |
| 하나의 row 위치               | `df.iloc[8]`            |           |
| row 위치의 리스트             | `df.iloc[[4, 5, 3]]`    |           |
| row 위치의 리스트 슬라이싱    | `df.iloc[2:5]`          | `df[2:5]` |
| 하나의 column 위치            | `df.iloc[:, 3]`         |           |
| column 위치의 리스트          | `df.iloc[:, [3, 5, 6]]` |           |
| column 위치의 리스트 슬라이싱 | `df.iloc[:, 3:7]`       |           |



## 데이터 변형하기

```python
# ex1)
import pandas as pd

df = pd.read_csv('data/body_imperial1.csv', index_col=0)

df.loc[1, 'Weight (Pound)'] = 200
df.drop(21, axis='index', inplace=True)
df.loc[20] = [70, 200]
# 출력
df

# ex2)
import pandas as pd
    
df = pd.read_csv('data/toeic.csv')

df['합격 여부'] = (df['LC'] >= 250) & (df['RC'] >= 250) & (df['LC'] + df['RC'] >= 600)
# 출력
df
```



## 큰 데이터 다루기

```python
# ex)
import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.
# 과목별 인원 가져오기
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

# 각 강의실 규모에 해당되는 과목 리스트 만들기
auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

# 강의실 이름 붙이기
for i in range(len(auditorium_list)):
    df.loc[(df["course name"] == sorted(auditorium_list)[i]) & allowed, "room assignment"] = "Auditorium-" + str(i + 1)

for i in range(len(large_room_list)):
    df.loc[(df["course name"] == sorted(large_room_list)[i]) & allowed, "room assignment"] = "Large-" + str(i + 1)
    
for i in range(len(medium_room_list)):
    df.loc[(df["course name"] == sorted(medium_room_list)[i]) & allowed, "room assignment"] = "Medium-" + str(i + 1)
    
for i in range(len(small_room_list)):
    df.loc[(df["course name"] == sorted(small_room_list)[i]) & allowed, "room assignment"] = "Small-" + str(i + 1)

# column 이름 바꾸기
df.rename(columns={"room assignment": "room number"}, inplace = True)
# 정답 출력
df
```



# 데이터 분석과 시각화

## 시각화 개요

- 데이터를 시각화해야 분석이 편하다

  - outlier 같은 값들도 한번에 알아볼 수 있고 인사이트를 얻기 좋다는 장점이 있다
  - 다른 사람들에게 보고를 할 때 이해하기 쉽고 관심을 얻기도 좋다

- ```python
  # ex1)
  %matplotlib inline
  import pandas as pd
  
  df = pd.read_csv('data/silicon_valley_summary.csv')
  
  # 코드를 작성하세요.
  boolean_male = df['gender']=='Male'
  boolean_manager = df['job_category'] == 'Managers'
  boolean_not_all = df['race_ethnicity'] != 'All'
  
  df[boolean_male & boolean_manager & boolean_not_all].plot(kind='bar', x='race_ethnicity',  y='count')
  ```

- 선 그래프, 막대 그래프, 파이 그래프, 히스토그램, 박스 플롯, 산점도 등 적절한 그래프를 사용하면 분석에 효율적이다



## Seaborn 시각화

- 다양한 그래프를 사용할 수 있는 라이브러리
- Statistical Data Visualization
- PDF(Probability Density Function)
  - 확률 밀도 함수
  - 히스토그램의 막대 갯수를 무한대로 늘려서 확률 밀도 함수를 추정할 수 있다
    - 다른 방법들도 있음(커널방법(kernel method), 국소가능도방법(local likelihood method))
  - 특정 구간의 확률은 그래프 아래 그 구간의 면적과 동일
- KDE(Kernel Density Estimation)
  - 확률 밀도 함수 추정법 중 하나
  - 갖고 있는 데이터를 바탕으로 확률 밀도 함수를 추정해준다
  - Seaborn 라이브러리로 히스토그램, 박스 플롯, 산점도 등에 PDF 관련 그래프를 그릴 수 있다. 산점도 같은 경우 등고선으로 표현된다



## 통계 분석

- 평균값 vs 중간값
  - 평균값은 잘못된 데이터의 영향을 크게 받는다. 예를 들어 엄청나게 큰 수가 잘못 들어왔을 때
  - 하지만 평균값이 더 좋은 인사이트를 주는 경우도 있다. 잘못된 데이터가 없다는 가정하에서 평점 평균 같은 경우 중간 값보다 좀더 좋은 결과를 줄 수 있으니까
- 피어슨 상관 계수
  - -1 ~ 1 까지의 계수를 가짐
  - 1은 확실한 상관 관계, 0은 관계 없음, -1은 반대의 상관 관계를 갖는다는 것을 의미한다



## Exploratory Data Analysis(EDA)

- 데이터 셋을 다양한 관점에서 살펴보고 탐색하면서 인사이트를 찾는 것

  - 각 row는 무엇을 의미하는가?
  - 각 column은 무엇을 의미하는가?
  - 각 column은 어떤 분포를 보이는가?
  - 두 column은 어떤 연관성이 있는가?
  - 등등

- EDA는 공식이 없다

  - 시각적인 방법, 통계적인 방법 등. 이 중 시각적인 방법이 많이 사용되는 편이다

- ```python
  # 상관관계를 통한 분석 예시
  import pandas as pd
  
  df = pd.read_csv('young_survey.csv')
  df.corr()
  
  brunch_df[1:19].sort_values(ascending=True)  # 음악 장르가 있는 1~18 column 골라서 정렬하기
  
  df.corr().loc['Writing notes', 'New environment']  # 가설 "메모를 자주 하는 사람들은 새로운 환경에 쉽게 적응할 것이다"의 상관 계수 구하기
  ```

- 클러스터 분석(Cluster Analysis)

  - 데이터를 특정 기준을 통해 클러스터를 구성해서 분석하는 것
  - 예를 들어 상관 관계가 높은 의학, 화학, 생물학을 좋아하는 사람들을 한 데 묶어서 분석하는 것



## 새로운 인사이트 발견하기

- 데이터 변형을 통해 새로운 데이터를 만들어내서 분석하는 방식

  - 새로운 column으로 모든 수치를 합한 Total 데이터를 만들거나, column 문자열 중 일부를 필터링하여 데이터를 만드는 경우, groupby로 카테고리를 만드는 경우, merge(inner join, left outer join, right outer join, full outer join)를 통해 데이터를 만드는 경우 등

- ```python
  # ex1) 문자열 다루기 예시
  import pandas as pd
  
  df = pd.read_csv('data/museum_2.csv')
  
  # 코드를 작성하세요.
  phone = df['운영기관전화번호'].str.split(pat='-', expand=True)  ## 문자열 포함 여부를 확인하는 method는 contains. ex) str.contains('대학교')
  df['지역번호'] = phone[0]
  df
  
  # ex2) dictionary를 통해 데이터 카테고리화 예시
  import pandas as pd
  
  df = pd.read_csv("data/museum_3.csv", dtype={'지역번호': str})
  
  # 코드를 작성하세요.
  region = {
      '02': '서울시',
      '031': '경기도', '032': '경기도',
      '033': '강원도', 
      '041': '충청도', '042': '충청도', '043': '충청도', '044': '충청도',
      '051': '부산시', 
      '052': '경상도', '053': '경상도', '054': '경상도', '055': '경상도',
      '061': '전라도', '062': '전라도', '063': '전라도',
      '064': '제주도',
      '1577': '기타', '070': '기타'
  }
  df["지역번호"] = df["지역번호"].map(region)
  df.rename(columns={"지역번호": "지역명"}, inplace=True)
  df
  
  # ex3) groupby method로 카테고리화 하는 예시
  import pandas as pd
  
  df = pd.read_csv('data/occupations.csv')
  
  # 코드를 작성하세요.
  occupation_group = df.groupby('occupation')
  df.loc[df['gender'] == 'M', 'gender'] = 0
  df.loc[df['gender'] == 'F', 'gender'] = 1
  occupation_group.mean()['gender'].sort_values(ascending=False)
  
  # ex4) merge로 데이터 join하는 예시
  import pandas as pd
  
  museum = pd.read_csv("data/museum_3.csv", dtype={'지역번호': str})
  number = pd.read_csv("data/region_number.csv", dtype={'지역번호': str})
  
  # 코드를 작성하세요.
  combined_df = pd.merge(museum, number, on='지역번호', how='left')
  combined_df
  ```



# 데이터 퀄리티 높이기

## 좋은 데이터의 기준

### 완결성

- 데이터에는 필수 항목과 선택 항목이 있다. 필수 항목은 모두 채워져 있어야 완결성이 있는 것이다
- 결측값이 있는지 확인하는 것으로 판단할 수 있다



### 유일성

- 동일한 데이터가 불필요하게 중복되어 있으면 안된다
  - 왜? 해당 데이터를 수정해야할 일이 있을 때 하나만 수정하고 다른 동일한 데이터를 수정하지 않으면 잘못된 정보가 기록되는 것이기 때문에
- ex) 회원 데이터를 예로 든다면, 이메일 인증이나 휴대폰 인증을 통해 데이터의 유일성을 유지할 수 있다



### 통일성(Conformity)

- 데이터가 동일한 형식으로 저장되어 있어야 한다
- 표기법, 단위, 기준, 언어 등을 형식으로 보고, 이를 일치시켜야 한다



### 정확성

- 데이터가 정확해야 한다
- 주로 데이터를 모으는 과정에서 일어난다
- 이상점 체크를 통해 정확한 데이터인지 재확인하는 과정이 필요하다
  - 이상점(Outlier): 다른 값들과 너무 동떨어져 있는 데이터. 어쩌면 부정확한 값일지도 모르는 데이터



## 데이터 클리닝

### 완결성

```python
# ex)
import pandas as pd

df = pd.read_csv('data/steam_1.csv')

df.dropna(inplace=True)  # df.dropna(axis='columns'), df.fillna(df.mean()) 등 여러 방법들이 있음

# 정답 출력
df
```



### 유일성

```python
# ex)
import pandas as pd

df = pd.read_csv('data/steam_1.csv')

df.drop_duplicates()  # row가 중복되면 삭제
df.T  # 행과 열 바꾸기
df.T.drop_duplicates()  # 이런 식으로 column 중복을 제거할 수 있음
df.drop_duplicates(subset='col1')  # 이런 식으로 중복을 판단할 column을 지정할 수 있음

# 정답 출력
df
```



### 정확성

- 이상점 기준

  - 절대적인 기준은 없고 다양한 방법이 사용된다
  - ex) IQR(Interquartile Range, 데이터의 75% 지점과 25% 지점 사이의 거리)를 사용하는 방법
    - pandas에서 기본 설정으로 ±1.5 * IQR 바깥에 있는 값들은 이상점으로 본다. 범위 조절 가능

- 관계적 이상점

  - 키 188cm: 충분히 존재 가능
  - 몸무게 42kg: 충분히 존재 가능
  - 키 188cm & 몸무게 42kg: 어려움. 이렇게 관계를 고려했을 때 이상점이라고 판단할 수도 있다

- 이상점이 제대로 된 데이터 라면?

  - 분석에 방해가 되면 제거하고, 의미 있는 정보라면 제거하지 않는다
  - 상황에 맞는 판단이 필요하다

- ```python
  # ex 1) IQR 기준 이상점 제거
  %matplotlib inline
  import pandas as pd
  
  df = pd.read_csv('data/movie_metadata.csv')
  
  # 코드를 작성하세요.
  q1 = df['budget'].quantile(0.25)
  q3 = df['budget'].quantile(0.75)
  iqr = q3 - q1
  
  condition = (df['budget'] > q3 + 5 * iqr)
  df.drop(df[condition].index, inplace=True)
  
  df.plot(kind='scatter', x='budget', y='imdb_score')
  
  # ex 2) 상위 값 기준 이상점 제거
  %matplotlib inline
  import pandas as pd
  
  df = pd.read_csv('data/movie_metadata.csv')
  
  # 코드를 작성하세요.
  drop_index = df['budget'].sort_values(ascending=False).head(15).index
  df.drop(drop_index, inplace=True)
  
  df.plot(kind='scatter', x= 'budget', y='imdb_score')
  ```



# 데이터 만들기

- 데이터를 활용하기 이전에 일단 각종 데이터를 잘 모으는 것이 중요하다!



## 데이터를 만드는 방법

### 데이터 다운로드

- 국내 사이트
  - 서울열린데이터광장: https://data.seoul.go.kr/
  - 공공데이터포털: https://www.data.go.kr
  - e-나라지표: http://www.index.go.kr/
  - 국가통계포털: http://kosis.kr
  - 서울특별시 빅데이터 캠퍼스: https://bigdata.seoul.go.kr/
  - 통계청: http://kostat.go.kr/
- 해외 사이트
  - 구글 데이터 검색: https://toolbox.google.com/datasetsearch
  - 캐글: https://www.kaggle.com/datasets
  - Awesome Public Datasets Github: https://github.com/awesomedata/awesome-public-datasets
  - Data and Story Library: https://dasl.datadescription.com/
  - 데이터허브: https://datahub.io/



### 센서 사용하기

- 센서: 물리적인 현상을 감지해서 전기 신호로 변환해 주는 장치
- 옷에 붙은 전자 태그 데이터, 기상청 데이터 등
- 아두이노, 라즈베리 파이 활용도 가능



### 웹에서 모으기

- 웹 스크래핑(Web Scraping)
  - 웹에서 내용을 긁어오는 것
- 웹 크롤링(Web Crawling)
  - crawl: (엎드려) 기다
  - 웹을 기어다니는 것
- 웹 크롤러: 웹 크롤링을 하며 웹 페이지 내용을 수집하는 프로그램



## 웹 페이지 가져오기





## 필요한 데이터 골라내기



