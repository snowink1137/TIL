import sys

sys.stdin = open('1244.txt', 'r')

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    information = list(map(int, input().split()))
    if information[0] == 1:
        where = information[1]
        cnt = 0
        while True:
            cnt += 1
            idx = (where * cnt) - 1
            if idx > N - 1:
                break
            else:
                if switch[idx] == 0:
                    switch[idx] = 1
                else:
                    switch[idx] = 0
    else:
        where = information[1]
        if switch[where-1] == 0:
            switch[where-1] = 1
        else:
            switch[where-1] = 0
        cnt = 0
        while True:
            cnt += 1
            idx1 = where - cnt - 1
            idx2 = where + cnt - 1
            if 0 > idx1 or idx2 > N - 1:
                break

            if switch[idx1] == 0:
                switch[idx1] = 1
            else:
                switch[idx1] = 0

            if switch[idx2] == 0:
                switch[idx2] = 1
            else:
                switch[idx2] = 0

result = ' '.join(map(str, switch))
print(result)
