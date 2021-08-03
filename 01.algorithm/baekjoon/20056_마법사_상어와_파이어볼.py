import sys
from collections import defaultdict

sys.stdin = open('20056_sample_input.txt')

result = 0
N, M, K = map(int, input().split())

directions = [
    [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]
]

fireballs = []
for _ in range(M):
    r, c, m, d, s = map(int, input().split())
    r -= 1
    c -= 1
    fireballs.append([r, c, m, d, s])

for _ in range(K):
    check_dict = defaultdict(list)
    for fireball in fireballs:
        r, c, m, s, d = fireball
        new_r, new_c = r + directions[d][0] * s, c + directions[d][1] * s

        while not (0 <= new_r < N and 0 <= new_c < N):
            if new_r < 0:
                new_r += N
            elif new_r >= N:
                new_r -= N

            if new_c < 0:
                new_c += N
            elif new_c >= N:
                new_c -= N

        check_dict[(new_r, new_c)].append([new_r, new_c, m, s, d])

    fireballs = []
    for key, value in check_dict.items():
        if len(value) == 1:
            fireballs.append(value[0][:])
        else:
            new_m, new_s = 0, 0
            is_odd, is_even = False, False
            for v in value:
                new_m += v[2]
                new_s += v[3]
                if v[4] % 2:
                    is_odd = True
                else:
                    is_even = True

            new_m = new_m // 5

            if not new_m:
                continue

            new_s = new_s // len(value)

            if (is_odd == True and is_even == False) or (is_odd == False and is_even == True):
                k = 0
            else:
                k = 1

            for i in range(4):
                fireballs.append([value[0][0], value[0][1], new_m, new_s, 2*i+k])


for fireball in fireballs:
    result += fireball[2]

print(result)
