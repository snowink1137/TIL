# 1. 트리의 높이를 계산해서 출력하시오.treeHeight(3) --> 3
# 2. 높이가 3 인 노드들을 출력하시오.(7, 8, 9, 10, 11)
# 3. 3 번 노드가 루트인 트리의 전체 노드수 treeSize(3) --> 8
# 4. 8번 노드와 10 번 노드의 공통조상을 출력하시오.(1, 3)
import sys

sys.stdin = open('tree_input.txt')

V, E = map(int, input().split())
arr = list(map(int, input().split()))
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

for i in range(0, E*2, 2):
    u, v = arr[i], arr[i+1]
    if L[u] == 0:
        L[u] = v
    else:
        R[u] = v

    P[v] = u


def tree_height(v, cnt=-1):
    if v == 0:
        return cnt

    height = tree_height(P[v], cnt+1)

    return height


def tree_size(v):
    global cnt
    if v == 0:
        return

    tree_size(L[v])
    tree_size(R[v])
    cnt += 1


def common_parent(v1, v2):
    p_v1 = v1
    p_v2 = v2
    cnt_1 = []
    cnt_2 = []
    while p_v1 != 0:
        p_v1 = P[p_v1]
        cnt_1.append(p_v1)

    while p_v2 != 0:
        p_v2 = P[p_v2]
        cnt_2.append(p_v2)

    result = []
    for i in cnt_1:
        if i in cnt_2:
            result.append(i)

    result.remove(0)
    return result


print(tree_height(4))

for i in range(1, 13):
    if tree_height(i) == 3:
        print(i, end=' ')

print()

cnt = 0
tree_size(3)
print(cnt)
print(common_parent(8, 10))

