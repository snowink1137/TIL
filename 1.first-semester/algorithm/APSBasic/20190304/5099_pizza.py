import sys
from queue import Queue

sys.stdin = open('5099_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    pizzas_enum = []
    for index, value in enumerate(pizzas):
        pizzas_enum.append([index, value])


    Q = Queue()
    for i in range(N):
        Q.put(pizzas_enum.pop(0))

    while Q.qsize() != 1:
        g = Q.get()
        if g[1] // 2 == 0 and len(pizzas_enum) > 0:
            Q.put(pizzas_enum.pop(0))
        elif g[1] // 2 != 0:
            h = [g[0], g[1]//2]
            Q.put(h)

    result = Q.get()
    print('#{} {}'.format(test_case, result[0]+1))
