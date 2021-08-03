import sys

sys.stdin = open('1924.txt', 'r')

x, y = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

day = y - 1
if x > 1:
    x -= 1
    while True:
        if x == 0:
            break

        day += days[x]
        x -= 1

print(week[day%7])
