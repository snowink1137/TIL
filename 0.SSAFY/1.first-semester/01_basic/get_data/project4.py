import requests
import datetime
import copy
import csv
import time
import urllib.request
import os


NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')

# csv 데이터 읽고 이미지 주소 리스트 만들기
movie_naver = open('movie_naver.csv', 'r', encoding='utf-8')
reader = csv.reader(movie_naver)

movie_img_url_list = []
movie_img_name_list = []
for line in reader:
    movie_img_name_list.append(line[0])
    movie_img_url_list.append(line[1])


del movie_img_url_list[0]
del movie_img_name_list[0]


client_id = NAVER_CLIENT_ID
client_secret = NAVER_CLIENT_SECRET
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}


for i, j in zip(movie_img_name_list, movie_img_url_list):
    urllib.request.urlretrieve(j, f'./images/{i}.jpg')
    