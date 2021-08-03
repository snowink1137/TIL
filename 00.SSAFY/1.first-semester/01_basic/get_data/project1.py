import requests
import datetime
import copy
import os

KOBIS_KEY = os.getenv('KOBIS_KEY')

# 10주 날짜 뽑기
dt = datetime.datetime(2019, 1, 13)
td = datetime.timedelta(7*10)
td_day = datetime.timedelta(7)
first_day_obj = dt - td
first_day = (first_day_obj).strftime('%Y%m%d')

day_obj = copy.deepcopy(first_day_obj)
days = [first_day]
for i in range(10):
    day_obj += td_day
    days.append(day_obj.strftime('%Y%m%d'))


del days[0]


# 영화진흥위원회 데이터 수집
## url list 만들기
key = KOBIS_KEY
weekGb = '0'
url_list = []
for target in days:
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?' + 'key=' + key + '&targetDt=' + target + '&weekGb=' + weekGb
    url_list.append(url)


## 박스오피스 100개 모으기
movie = ['movie_code', 'title', 'audience', 'recorded_at']
for url in url_list:
    response = requests.get(url)
    movie_data = response.json()
    for i in range(10):
        movie.append(movie_data['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'])
        movie.append(movie_data['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm'])
        movie.append(movie_data['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc'])
        movie.append(movie_data['boxOfficeResult']['showRange'][9:])


## 박스오피스 중복 제거하기
movie_result = ['movie_code', 'title', 'audience', 'recorded_at']
movie_code_list = []
for i in range(100):
    movie_code_index = 400 - 4*i
    title_index = movie_code_index + 1
    audience_index = title_index + 1
    recorded_at_index = audience_index + 1

    if movie[movie_code_index] in movie_code_list:
        continue
    else:
        movie_result.append(movie[movie_code_index])
        movie_result.append(movie[title_index])
        movie_result.append(movie[audience_index])
        movie_result.append(movie[recorded_at_index])
        movie_code_list.append(movie[movie_code_index])


# 파일로 내보내기
import csv
f = open('boxoffice.csv', 'a+', encoding='utf-8', newline='')
for i in range(44):
    writer = csv.writer(f)
    writer.writerow(
        [movie_result[4*i + 0], movie_result[4*i + 1], movie_result[4*i + 2], movie_result[4*i + 3]]
    )


f.close()

