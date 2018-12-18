import random
import requests

## pick my lotto number
numbers = list(range(1,46))

my_numbers = random.sample(numbers, 6)
my_numbers.sort()
print(my_numbers)


## get my lotto number
url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json()

real_numbers = []
for key in lotto_data:
    if 'drwt' in key:
        real_numbers.append(lotto_data[key])

real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)

'''
    mission : 등수 골라내기
    1등 : my_numbers == real_numbers
    2등 : real & my 가 5개 같고, my 나머지 하나가 bonus와 같을 때
    3등 : real & my 가 4개
    4등 : real & my 가 3개
    5등 : real & my 가 2개
    6등 : real & my 가 1개
'''

