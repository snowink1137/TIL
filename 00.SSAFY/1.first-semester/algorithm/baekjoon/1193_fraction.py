import sys

sys.stdin = open('1193.txt')

X = int(input())

cnt = 1
pre_value = 1
after_value = 1
while True:
    if pre_value <= X < after_value:
        group = cnt - 1
        break

    cnt += 1
    pre_value = after_value
    after_value = 1 + int((cnt-1) * cnt / 2)

if group % 2:
    difference = X - pre_value
    up = group - difference
    down = group + 1 - up
    print('{}{}{}'.format(up, '/', down))
else:
    difference = X - pre_value
    up = group - difference
    down = group + 1 - up
    print('{}{}{}'.format(down, '/', up))
