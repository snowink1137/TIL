import sys

sys.stdin = open('21608_sample_input.txt', 'r')

from collections import defaultdict

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0

N = int(input())
students = []
likes = defaultdict(list)
for _ in range(N**2):
    a, b, c, d, e = map(int, input().split())
    students.append(a)
    likes[a].append(b)
    likes[a].append(c)
    likes[a].append(d)
    likes[a].append(e)

matrix = [[0 for _ in range(N)] for _ in range(N)]
empty_seats = set()
seated_student = dict()
for i in range(N):
    for j in range(N):
        empty_seats.add((i, j))


def check_like(student, seated_student, likes, empty_seats, matrix):
    candidates = []

    liked_students = []
    for candidate in likes[student]:
        if seated_student.get(candidate):
            liked_students.append(candidate)

    if not liked_students:
        return list(empty_seats)

    for liked_student in liked_students:
        r, c = seated_student[liked_student][0], seated_student[liked_student][1]
        for i in range(4):
            x, y = r + dx[i], c + dy[i]
            if not (0 <= x < N and 0 <= y < N):
                continue

            if matrix[x][y]:
                continue

            candidates.append((x, y))

    if not candidates:
        return list(empty_seats)

    candidates_dict = defaultdict(int)
    for candidate in candidates:
        candidates_dict[candidate] += 1

    cnt_max = max(candidates_dict.values())
    new_candidates = []
    for k, v in candidates_dict.items():
        if v == cnt_max:
            new_candidates.append(k)

    return new_candidates


def check_empty(candidates, matrix):
    cnt_max = -1
    new_candidates = []

    for candidate in candidates:
        cnt = 0
        for i in range(4):
            x, y = candidate[0] + dx[i], candidate[1] + dy[i],
            if not (0 <= x < N and 0 <= y < N):
                continue

            if matrix[x][y]:
                continue

            cnt += 1

        if cnt == cnt_max:
            new_candidates.append(candidate)
        elif cnt > cnt_max:
            cnt_max = cnt
            new_candidates = [candidate]

    return new_candidates


for student in students:
    candidates = check_like(student, seated_student, likes, empty_seats, matrix)
    if len(candidates) == 1:
        seated_student[student] = candidates[0]
        matrix[candidates[0][0]][candidates[0][1]] = student
        empty_seats.remove((candidates[0][0], candidates[0][1]))
        continue

    candidates = check_empty(candidates, matrix)
    if len(candidates) == 1:
        seated_student[student] = candidates[0]
        matrix[candidates[0][0]][candidates[0][1]] = student
        empty_seats.remove((candidates[0][0], candidates[0][1]))
        continue

    candidates.sort(key=lambda x: (x[0], x[1]))
    seated_student[student] = candidates[0]
    matrix[candidates[0][0]][candidates[0][1]] = student
    empty_seats.remove((candidates[0][0], candidates[0][1]))

for i in range(N):
    for j in range(N):
        cnt = 0
        student = matrix[i][j]
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not (0 <= x < N and 0 <= y < N):
                continue

            friend = matrix[x][y]
            if friend in likes[student]:
                cnt += 1

        if cnt == 0:
            continue

        answer += 10 ** (cnt-1)

print(answer)
