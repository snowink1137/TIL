import requests
import os

KOBIS_KEY = os.getenv('KOBIS_KEY')
NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')


key = KOBIS_KEY
targetDt = '20190113'
weekGb = '0'

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?' + 'key=' + key + '&targetDt=' + targetDt + '&weekGb=' + weekGb

data = requests.get(url).json()
print(data['boxOfficeResult']['dailyBoxOfficeList'][0]['movieNm'])



# 네이버
movies = ['말모이', '주먹왕랄프', '보헤미안 랩소디']
naver_uri = 'https://openapi.naver.com/v1/search/movie.json?query='
client_id = NAVER_CLIENT_ID
client_secret = NAVER_CLIENT_SECRET
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

res = requests.get(naver_uri + movies[0], headers = headers)
data = res.json()

result = []
for movie in movies:
    data_set = requests.get(naver_uri + movie, headers = headers).json()
    movie_info = {}
    movie_info['name'] = data_set['items'][0]['title']
    movie_info['link'] = data_set['items'][0]['link']
    movie_info['image'] = data_set['items'][0]['image']
    result.append(movie_info)


