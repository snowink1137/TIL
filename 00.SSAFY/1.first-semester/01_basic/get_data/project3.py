import requests
import datetime
import copy
import csv
import time
import os


NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')

# csv 데이터 읽고 영화 이름 리스트 만들기
boxoffice = open('boxoffice.csv', 'r', encoding='utf-8')
reader = csv.reader(boxoffice)

movie_name_list = []
for line in reader:
    movie_name_list.append(line[1])


del movie_name_list[0]

# csv 데이터 읽고 영화 code 리스트 만들기
boxoffice = open('boxoffice.csv', 'r', encoding='utf-8')
reader = csv.reader(boxoffice)

movie_code_list = []
for line in reader:
    movie_code_list.append(line[0])


del movie_code_list[0]


# 네이버 요청 결과 data list 만들기
naver_uri = 'https://openapi.naver.com/v1/search/movie.json?query='
client_id = NAVER_CLIENT_ID
client_secret = NAVER_CLIENT_SECRET
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}
naver_data_list = []
for i in range(43):
    res = requests.get(naver_uri + movie_name_list[i], headers = headers)
    data = res.json()
    naver_data_list.append(data)
    print(i, '완료')
    time.sleep(2)


# 원하는 데이터 리스트로 저장
movie_naver = ['영진위 영화 대표코드', '영화 썸네일 이미지의 URL', '하이퍼텍스트 link', '유저 평점']
j = 0
for i in naver_data_list:
    movie_naver.append(movie_code_list[j])
    movie_naver.append(i['items'][0]['image'])
    movie_naver.append(i['items'][0]['link'])
    movie_naver.append(i['items'][0]['userRating'])
    j += 1
    print(i, '완료')


# 파일로 저장
f = open('movie_naver.csv', 'a+', encoding='utf-8', newline='')
for i in range(44):
    writer = csv.writer(f)
    writer.writerow(
        [movie_naver[4*i + 0], movie_naver[4*i + 1], movie_naver[4*i + 2], movie_naver[4*i + 3]]
    )

f.close()

