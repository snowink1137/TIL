import sys

sys.stdin = open('4864_sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    p = input()
    t = input()

    result = 0
    m, n = len(p), len(t)
    for i in range(n-m+1):
        for j in range(m):
            if t[i+j] != p[j]:
                break
        else:
            result = 1
            break

    print(f'#{test_case} {result}')
