arr = [55, 7, 78, 12 ,42]
N = len(arr)
for j in range(N-1, 0, -1):
    for i in range(j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)
