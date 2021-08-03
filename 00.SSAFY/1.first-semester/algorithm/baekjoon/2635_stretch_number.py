import sys
from collections import deque

sys.stdin = open('2635.txt', 'r')

N = int(input())

result = 1
result_list = [N]

first = N
while True:
    if first <= 0:
        break

    temp = deque()
    temp.append(N)
    temp.append(first)
    while True:
        nxt = temp[-2] - temp[-1]
        if nxt < 0:
            length = len(temp)
            if length > result:
                result_list = temp
                result = length

            break

        temp.append(nxt)

    first -= 1

print(result)
print(' '.join(map(str, result_list)))
