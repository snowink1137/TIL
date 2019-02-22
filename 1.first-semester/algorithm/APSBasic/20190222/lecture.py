# # 피보나치 수 DP, memoization 적용
# memo = [0] * 101
# memo[0] = 0
# memo[1] = 1
#
# for i in range(2, 41):
#     memo[i] = memo[i-1] + memo[i-2]
#
# print(memo[40])

# 그래프 정보를 메모리에 저장하고 DFS 방식으로 탐색하기
import sys
sys.stdin = open('DFS_input.txt')


def DFS(start):
    visit = [False for _ in range(V+1)]
    S = []
    v = start
    visit[v] = True
    print(v, end=' ')
    S.append(v)
    # stack이 비지 않아 있을 때까지 실행한다.
    while len(S) > 0:
        # v의 방문하지 않은 인접 정점을 찾는다.
        goback = True
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                print(w, end=' ')
                S.append(v)
                v = w
                goback = False
                break

        if goback:
            v = S.pop(-1)


V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V+1):
    print(i, G[i])

DFS(1)
