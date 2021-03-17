import sys

sys.stdin = open('20058_sample_input.txt', 'r')

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

result1 = 0
result2 = 0

N, Q = map(int, input().split())

ice_map = []
for i in range(2**N):
    ice_map.append(list(map(int, input().split())))

firestorms = list(map(int, input().split()))




print(result1)
print(result2)
