import requests
import datetime
import copy
import csv
import os

KOBIS_KEY = os.getenv('KOBIS_KEY')


# csv 데이터 읽고 영화 code 리스트 만들기
boxoffice = open('boxoffice.csv', 'r', encoding='utf-8')
reader = csv.reader(boxoffice)

movie_code_list = []
for line in reader:
    movie_code_list.append(line[0])


del movie_code_list[0]


# 영화진흥위원회 데이터 수집
## url list 만들기
key = KOBIS_KEY
weekGb = '0'
url_list = []
for code in movie_code_list:
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?' + 'key=' + key + '&movieCd=' + code
    url_list.append(url)


## 상세 정보 데이터 수집
movie_data = ['영화 대표코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '개봉연도', '상영시간', '장르', '감독명', '배우1', '배우2', '배우3']

for url in url_list:
    response = requests.get(url)
    response_json = response.json()
    movie_data.append(response_json['movieInfoResult']['movieInfo']['movieCd'])
    movie_data.append(response_json['movieInfoResult']['movieInfo']['movieNm'])
    movie_data.append(response_json['movieInfoResult']['movieInfo']['movieNmEn'])
    movie_data.append(response_json['movieInfoResult']['movieInfo']['movieNmOg'])
    movie_data.append(response_json['movieInfoResult']['movieInfo']['prdtYear'])
    movie_data.append(response_json['movieInfoResult']['movieInfo']['showTm'])
    movie_data.append(response_json['movieInfoResult']['movieInfo']['genres'][0]['genreNm'])
    movie_data.append(response_json['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'])
    if len(response_json['movieInfoResult']['movieInfo']['actors']) > 2:
        movie_data.append(response_json['movieInfoResult']['movieInfo']['actors'][0]['peopleNm'])
        movie_data.append(response_json['movieInfoResult']['movieInfo']['actors'][1]['peopleNm'])
        movie_data.append(response_json['movieInfoResult']['movieInfo']['actors'][2]['peopleNm'])
    elif len(response_json['movieInfoResult']['movieInfo']['actors']) == 2:
        movie_data.append(response_json['movieInfoResult']['movieInfo']['actors'][0]['peopleNm'])
        movie_data.append(response_json['movieInfoResult']['movieInfo']['actors'][1]['peopleNm'])
        movie_data.append('')
    elif len(response_json['movieInfoResult']['movieInfo']['actors']) == 1:
        movie_data.append(response_json['movieInfoResult']['movieInfo']['actors'][0]['peopleNm'])
        movie_data.append('')
        movie_data.append('')
    elif len(response_json['movieInfoResult']['movieInfo']['actors']) == 0:
        movie_data.append('')
        movie_data.append('')
        movie_data.append('')


f = open('movie.csv', 'a+', encoding='utf-8', newline='')
for i in range(44):
    writer = csv.writer(f)
    writer.writerow(
        [movie_data[11*i + 0], movie_data[11*i + 1], movie_data[11*i + 2], movie_data[11*i + 3], movie_data[11*i + 4], movie_data[11*i + 5], movie_data[11*i + 6], movie_data[11*i + 7], movie_data[11*i + 8], movie_data[11*i + 9], movie_data[11*i + 10]]
    )


f.close()



