import sys


sys.stdin = open('1208_sample_input.txt')

for test_case in range(1, 11):
    N = int(input())

    height_list = list(map(int, input().split()))
    height_count = [0] * 101

    low_height = 100
    high_height = 1
    for height in height_list:
        height_count[height] += 1
        if height > high_height:
            high_height = height
        elif height < low_height:
            low_height = height

    for i in range(N):
        if low_height == high_height:
            print(f'#{test_case} 0')

        height_count[high_height] -= 1
        height_count[high_height-1] += 1
        if height_count[high_height] == 0:
            high_height -= 1

        height_count[low_height] -= 1
        height_count[low_height+1] += 1
        if height_count[low_height] == 0:
            low_height += 1

    print(f'#{test_case} {high_height-low_height}')
