import sys

sys.stdin = open('12100.txt', 'r')

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

