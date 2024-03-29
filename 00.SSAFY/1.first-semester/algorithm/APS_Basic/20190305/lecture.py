# 1. 트리 순회(전위, 중위, 후위)
import sys

sys.stdin = open('tree_input.txt')


def inorder(v):
    if v == 0:
        return

    # print 순서에 따라 중위 순회, 전위 순회, 후위 순회로 바꿀 수 있다!
    # 앞에 놓으면 전위 순회, 중간에 놓으면 중위 순회, 끝에 놓으면 후위 순회!
    print(v, end=' ')
    inorder(L[v])
    inorder(R[v])



# 트리 입력
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

inorder(1)


# 2. 트리 순회(전역 변수 안 쓰고 return 사용하는 방법 예시)
def inorder(v):
    if v == 0:
        return 0

    l = inorder(L[v])
    r = inorder(R[v])
    return l + r + 1


print()
print(inorder(1))