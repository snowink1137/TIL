import csv

# 있어야만 open하는 것이아니고 없으면 만들어서 연다.
# 'a+', 'w+' 등의 옵션 있는데 한번 찾아보길.
# csv 쓰기 실습
f = open('ss3.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(
    ['황은석', '강진우']
)
f.close()

# csv 읽기 실습
f_r = open('ss3.csv', 'r', encoding='utf-8')
reader = csv.reader(f_r)

for line in reader:
    print(type(line), line)

