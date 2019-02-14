data = [7, 4, 2, 0, 0, 6, 0, 7, 0]

maxH = 0
for i in range(len(data)):
    H = len(data) - i - 1
    for j in range(i + 1, len(data)):
        if data[i] <= data[j]:
            H -= 1

    maxH = max(H, maxH)

print(data)
print(maxH)