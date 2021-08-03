import sys

sys.stdin = open('5648.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    information = [list(map(int, input().split())) for _ in range(N)]

