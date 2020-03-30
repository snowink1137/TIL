import requests

{
    "drwtNo1":2,
    "drwtNo2":25,
    "drwtNo3":28,
    "drwtNo4":30,
    "drwtNo5":33,
    "drwtNo6":45,
    "bnusNo":6
}

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


# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6']
# ]

# print(real_numbers)