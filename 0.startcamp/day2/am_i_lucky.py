import random
import requests

## pick my lotto number
numbers = list(range(1,46))
my_numbers = random.sample(numbers, 6)
my_numbers.sort()



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


'''
    mission : 등수 골라내기
    1등 : my_numbers == real_numbers
    2등 : real & my 가 5개 같고, my 나머지 하나가 bonus와 같을 때
    3등 : real & my 가 4개
    4등 : real & my 가 3개
    5등 : real & my 가 2개
    6등 : real & my 가 1개

    테스트 케이스 두고 시작하면 좋다고 하심.
'''
# # 테스트 케이스
# my_numbers = set([12,7,8,9,10,11])
# real_numbers = set([1,2,3,4,5,6])
# bonus_number = 10

print('내가 선택한 번호 :', my_numbers)
print('실제 당첨 번호 :', real_numbers)

my_numbers = set(my_numbers)
real_numbers = set(real_numbers)

if len(my_numbers.intersection(real_numbers)) == 6:
    print('축하합니다. 1등 입니다!')
elif len(my_numbers.intersection(real_numbers)) == 5:
    if bonus_number in my_numbers:
        print('축하합니다. 2등 입니다!')
    else:
        print('축하합니다. 3등 입니다!')    
elif len(my_numbers.intersection(real_numbers)) == 4:
    print('축하합니다. 4등 입니다!')
elif len(my_numbers.intersection(real_numbers)) == 3:
    print('축하합니다. 5등 입니다!')
elif len(my_numbers.intersection(real_numbers)) == 2:
    print('축하합니다. 6등 입니다!')
elif len(my_numbers.intersection(real_numbers)) == 1:
    print('축하합니다. 7등 입니다!')
else:
    print('당첨되지 않았습니다. 다음에 도전해주세요!')