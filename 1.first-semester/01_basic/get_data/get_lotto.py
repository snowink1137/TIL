"""
https://www.dhlottery.co.kr/common.do
?
method=getLottoNumber
&
drwNo=837
"""
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

got = requests.get(url)
print(got)