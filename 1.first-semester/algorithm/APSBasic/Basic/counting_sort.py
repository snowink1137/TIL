K = 4
arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0] * (K + 1)
sorted1 = [0] * len(arr)
sorted2 = [0] * len(arr)

# 빈도 수 계산
for val in arr:
    cnt[val] += 1

print(cnt)

# 정렬
idx = 0
for i in range(K+1):
    for j in range(cnt[i]):
        sorted1[idx] = i
        idx += 1

print(sorted1)

# 교재에 있는 정렬 방법
for i in range(1, K+1):
    cnt[i] = cnt[i-1] + cnt[i]

for i in range(len(arr)-1, -1, -1):
    cnt[arr[i]] -= 1
    sorted2[cnt[arr[i]]] = arr[i]

print(sorted2)
