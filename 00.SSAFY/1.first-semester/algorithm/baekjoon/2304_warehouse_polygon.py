import sys

sys.stdin = open('2304.txt', 'r')

N = int(input())

information = []
for _ in range(N):
    information.append(list(map(int, input().split())))

max_value = max(information, key=lambda x: x[1])
max_list = [x[0] for x in information if x[1] == max_value[1]]
information.sort(key=lambda x: x[0])

if len(max_list) == 1:
    max_block = max_value[1]
else:
    max_list.sort()
    max_block = (max_list[-1] - max_list[0] + 1) * max_value[1]

result = 0
result += max_block

left_index = information.index([max_list[0], max_value[1]])
right_index = information.index([max_list[-1], max_value[1]])


current = information[0][0]
height = information[0][1]
for i in range(left_index):
    if information[i+1][1] >= height:
        result += (information[i+1][0] - current) * height
        current = information[i+1][0]
        height = information[i+1][1]

current = information[-1][0]
height = information[-1][1]
for j in range(len(information)-1, right_index, -1):
    if information[j-1][1] >= height:
        result += (current - information[j-1][0]) * height
        current = information[j-1][0]
        height = information[j-1][1]

print(result)
