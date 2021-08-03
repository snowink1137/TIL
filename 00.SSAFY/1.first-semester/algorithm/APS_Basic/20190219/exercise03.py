matrix = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]
# 배열 만들기
arr = []
for row in matrix:
    arr += row

N = len(arr)

# 버블 정렬
for i in range(N-1, -1, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# 나열
result = [[0]*5 for _ in range(5)]

direction = 1
total = 5
x = 0
y = 0
cnt = 0
while True:
    if direction % 2 == 0:
        total -= 1

    if total == 0:
        break

    if direction == 1:
        for _ in range(total):
            result[x][y] = arr[cnt]
            cnt += 1
            y += 1

        direction = 2
        y -= 1
        x += 1
    elif direction == 2:
        for _ in range(total):
            result[x][y] = arr[cnt]
            cnt += 1
            x += 1

        direction = 3
        x -= 1
        y -= 1
    elif direction == 3:
        for _ in range(total):
            result[x][y] = arr[cnt]
            cnt += 1
            y -= 1

        direction = 4
        y += 1
        x -= 1
    elif direction == 4:
        for _ in range(total):
            result[x][y] = arr[cnt]
            cnt += 1
            x -= 1

        direction = 5
        x += 1
        y += 1
    elif direction == 5:
        for _ in range(total):
            result[x][y] = arr[cnt]
            cnt += 1
            y += 1

        direction = 2
        y -= 1
        x += 1

print(result)
