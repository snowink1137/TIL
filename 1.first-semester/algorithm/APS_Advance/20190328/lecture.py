# # 1. merge sort (아직 미완성)
# arr = [0,1,3,2,6,9,5,6]
# temp = [0] * len(arr)
#
#
# def merge_sort(lo, hi):
#     if lo == hi:
#         return
#
#     mid = (lo + hi) >> 1
#
#     merge_sort(lo, mid)
#     merge_sort(mid + 1, hi)
#     i, j, k = lo, mid + 1, lo
#     while i <= mid and j <= hi:
#         if arr[i] < arr[j]:
#             temp[k] = arr[i]
#             k, i = k + 1, i + 1
#         else:
#             temp[k] = arr[j]
#             k, j = k + 1, j + 1
#
#     while i <= mid:
#         temp[k] = arr[i]
#         k, i = k + 1, i + 1
#
#     while j <= hi:
#         temp[k] = arr[j]
#         k, j = k + 1, j + 1
#
#
# merge_sort(0, len(arr)-1)
# print(temp)

#2. MST(최소 신장 트리)
p = [i for i in range(10)]


def findset(x):
    if x != p[x]:
        p[x] = findset(p[x])

    return p[x]


def union(x, y):
    p[y] = x


V, E = map(int, input().split())
edges = []
tree = []
for i in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

edges.sort(key=lambda x: x[2])
cnt = V - 1
while cnt > 0:
    u, v, w = edges.pop(0)
    a = findset(u)
    b = findset(v)
    if a == b:
        continue
    tree.append((u, v, w))
    union(a, b)
    cnt -= 1
