arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

sum = 0
for i in range(5):
    for j in range(5):
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x <= 4 and 0 <= y <= 4:
                sum += abs(arr[i][j] - arr[x][y])

result = sum / 2
print(result)
