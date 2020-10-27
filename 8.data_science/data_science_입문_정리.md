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

### DataFrame 인덱싱

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



### 데이터 변형하기

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



### 큰 데이터 다루기





# 데이터 분석과 시각화



# 데이터 퀄리티 높이기



# 데이터 만들기





