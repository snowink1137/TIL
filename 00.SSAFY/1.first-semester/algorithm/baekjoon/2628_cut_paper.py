import sys

sys.stdin = open('2628.txt', 'r')

width, height = map(int, input().split())
N = int(input())

row = [0]
column = [0]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        row.append(b)
    else:
        column.append(b)

row.append(height)
column.append(width)
row.sort()
column.sort()

row_max = 0
for i in range(len(row)-1):
    temp = row[i+1] - row[i]
    if temp > row_max:
        row_max = temp

column_max = 0
for i in range(len(column)-1):
    temp = column[i+1] - column[i]
    if temp > column_max:
        column_max = temp

print(row_max*column_max)
