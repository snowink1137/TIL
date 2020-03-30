# # 1. 원소별로 들어가는지 안들어가는지 체크하는 방식 중, binary counting 말고 중첩된 for 문을 활용해서 부분 집합 구하기
# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             print(i, j, k)


# # 2. 원소별로 들어가는지 안들어가는지 체크하는 방식 중, binary counting 말고 재귀 호출을 활용해서 부분 집합 구하기(위의 코드의 중첩된 for 문을 재귀 호출로 교체한 것)
# bits = [0] * 3
#
#
# def subset(k, n):
#     if k == n:    # 단말 노드에 도달 했을 때. 모든 선택이 끝난 경우.
#         print(bits)
#     else:           # 아직 선택할 것이 남아 있는 경우.
#         # 선택지(자식 노드)의 수만큼 재귀호출을 해야 한다.
#         for i in range(2):
#             bits[k] = i
#             subset(k+1, n)
#
#
# subset(0, 3)  # 0: 시작 상태, 3: 단말 노드의 높이
#                 # 선택 수 = 0, 해야할 선택 수 = 3


# # 3. 순열 구하기(for 문 중첩)
# arr = 'ABC'
# N = len(arr)
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         for k in range(N):
#             if k == i or k == j:
#                 continue
#             print(arr[i], arr[j], arr[k])


# # 4. 순열 구하기(for문 중첩을 재귀 호출로 바꾼 버전)
# arr = 'ABC'
# N = len(arr)
# order = [0] * N
#
#
# def perm(k, n): # k: 시작 상태, n: 단말 노드의 높이
#     if k == n:
#         # order[] 저장된 순서를 확인
#         print(order)
#         return
#
#     visit = [False] * N
#     for i in range(k):
#         visit[order[i]] = True
#
#     for i in range(n):
#         if visit[i]:
#             continue
#
#         order[k] = i
#         perm(k+1, n)
#
#
# perm(0, 3)  # 3: 요소 수(단말 노드의 높이)


# 5. 순열 구하기(재귀 호출로 바꾼 버전을 다른 방식으로 수정한 것. visit 정보를 비트 표현 및 비트 연산자 사용하여 간단하게 만들기 + 이전 정보를 전역 변수가 아닌 매개 변수로 전달하는 버전.)
arr = 'ABC'
N = len(arr)
order = [0] * N


def perm(k, n, visit): # k: 시작 상태, n: 단말 노드의 높이
    if k == n:
        # order[] 저장된 순서를 확인
        print(order)
        perm_list.append(order)
        return

    for i in range(n):
        if visit & (1 << i):
            continue

        order[k] = i
        perm(k+1, n, visit | (1 << i))

perm_list = []
perm(0, N, 0)  # 3: 요소 수(단말 노드의 높이)
print(perm_list)
