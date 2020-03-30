# 1. 평균을 구하시오
my_score = [79, 84, 66, 93]
my_average = sum(my_score) / len(my_score)
print('나와 당신의 평균 점수')
print('나의 평균 점수 : ', my_average)

your_score = {
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100
}
your_average = sum(your_score.values()) / len(your_score)
print('당신의 평균 점수 : ', your_average)
print()
print('values() 메소드의 반환 타입 : ', type(your_score.values()))
print()


# 3. 도시별 온도 평균
# 서울: ?
# 대전: ?
# 광주: ?
# 구미: ?

# 4: 도시 중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳.
# Hottest: ??, Coldest: ??

cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}
print('지역별 평균 온도')
cities_average_temp_3days = {}
for key, value in cities_temp.items():
    average_temp = round(sum(value) / len(value), 2)
    #print(key, ':', average_temp, '도')
    print('{0}: {1}도'.format(key, average_temp))
    cities_average_temp_3days[key] = average_temp


print()

max_temp = max(cities_average_temp_3days.values())
min_temp = min(cities_average_temp_3days.values())

max_temp_key = set()
min_temp_key = set()
for key, value in cities_average_temp_3days.items():
    if value == max_temp:
        max_temp_key.add(key)
    elif value == min_temp:
        min_temp_key.add(key)

print('평균 온도 기준')
print('Hottest:', max_temp_key, 'Coldest:', min_temp_key)
print()

cities_maxmin_temp = {}
for key, value in cities_temp.items():
    max_iter = max(value)
    min_iter = min(value)
    cities_maxmin_temp[key] = (max_iter, min_iter)


# print(cities_maxmin_temp)

hottest = max(sum(cities_maxmin_temp.values(), ()))
coldest = min(sum(cities_maxmin_temp.values(), ()))
# print(hottest, coldest)
hottest_key = set()
coldest_key = set()
for key, value in cities_maxmin_temp.items():
    if hottest in value:
        hottest_key.add(key)
    elif coldest in value:
        coldest_key.add(key)

print('개별 온도 기준')
print('Hottest:', hottest_key, 'Coldest:', coldest_key)
    
