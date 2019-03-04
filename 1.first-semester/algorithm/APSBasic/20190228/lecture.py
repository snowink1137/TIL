# # 1. Queue 자료 구조 직접 구현
# # 이런 방식으로 하지 않고 list로 그냥 동적할당해서 쓰면 자료가 클 경우 매우 느려질 수 있음.
# # 자료가 크면 front, rear 개념 구현해서 쓰는 것이 좋다.
# # 물론 파이썬에서 제공하는 모듈도 있다. deque 자료 구조가 제일 빠르다고 공식 문서에 나와있다고 하심.
# QSIZE = 100
# Q = [0] * QSIZE
# front = rear - 1
#
#
# def push(item):
#     global rear
#     rear += 1
#     Q[rear] = item
#
#
# def pop():
#     global front
#     front += 1
#     return Q[front]
#
#
# def empty():
#     return front == rear
#
#
# for i in range(5):
#     push(i)
#
# while not empty():
#     print(pop())


# 2. Queue를 활용하여 BFS 구현하기
from queue import Queue


def BFS(s, G):
    visit = [False] * (V + 1)
    D = [0] * (V + 1)  # 간선의 Distance 기록 배열
    P = [0] * (V + 1)  # Path 기록 배열

    Q = Queue()
    Q.put(s)
    visit[s] = True
    print(s, end=" ")
    while not Q.empty():
        v = Q.get()
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1  # 각 간선의 가중치가 1인 경우. 가중치가 1 이상인 경우는 알고리즘이 달라져야 함.
                P[w] = v
                visit[w] = True
                Q.put(w)
                print(w, end=" ")
    print()
    return D
# ----------------------------------------------


import sys
sys.stdin = open("BFS_input.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


D = BFS(1, G)
print(D[1:])

