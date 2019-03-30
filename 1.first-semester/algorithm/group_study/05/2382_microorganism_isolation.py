import sys

sys.stdin = open('2382.txt', 'r')


class Micro:
    def __init__(self, x, y, number, direction):
        self.x = x
        self.y = y
        self.number = number
        self.direction = direction

    def go(self):
        # global MAP
        if MAP[self.x][self.y] is self:
            MAP[self.x][self.y] = False

        if self.direction == 1:
            self.x += -1
            if self.x == 0:
                self.direction = 2
                self.number //= 2

            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].number > self.number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self
            else:
                MAP[self.x][self.y] = self

        elif self.direction == 2:
            self.x += 1
            if self.x == N-1:
                self.direction = 1
                self.number //= 2

            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].number > self.number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self
            else:
                MAP[self.x][self.y] = self
        elif self.direction == 3:
            self.y += -1
            if self.y == 0:
                self.direction = 4
                self.number //= 2

            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].number > self.number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self
            else:
                MAP[self.x][self.y] = self
        elif self.direction == 4:
            self.y += 1
            if self.y == N-1:
                self.direction = 3
                self.number //= 2

            if not MAP[self.x][self.y]:
                MAP[self.x][self.y] = self
            elif visit[MAP[self.x][self.y].x][MAP[self.x][self.y].y]:
                if MAP[self.x][self.y].number > self.number:
                    MAP[self.x][self.y].number += self.number
                else:
                    self.number += MAP[self.x][self.y].number
                    MAP[self.x][self.y] = self
            else:
                MAP[self.x][self.y] = self


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    object_list = [0] * K
    for i in range(K):
        x, y, number, direction = map(int, input().split())
        object_list[i] = Micro(x, y, number, direction)

    MAP = [[False] * N for _ in range(N)]
    for _ in range(M):
        visit = [[False] * N for _ in range(N)]
        temp = []
        for i in range(len(object_list)):
            object_list[i].go()
            if not visit[object_list[i].x][object_list[i].y]:
                visit[object_list[i].x][object_list[i].y] = True
                temp.append([object_list[i].x, object_list[i].y])

        object_list = []
        for t in temp:
            object_list.append(MAP[t[0]][t[1]])

    result = 0
    for o in object_list:
        result += o.number

    print('#{} {}'.format(test_case, result))
