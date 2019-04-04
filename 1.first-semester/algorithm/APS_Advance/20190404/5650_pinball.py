import sys

sys.stdin = open('test.txt', 'r')


class Pinball:
    def __init__(self, i, j, k):
        self.original_x = i
        self.original_y = j
        self.x = i
        self.y = j
        self.direction = k

    def game(self):
        cnt = 0
        while True:
            self.go()
            if (self.x == self.original_x and self.y == self.original_y) or matrix[self.x][self.y] == -1:
                break
            elif matrix[self.x][self.y] == -2:
                cnt += 1
                self.change_direction(self.direction, 5)
            elif 1 <= matrix[self.x][self.y] <= 5:
                cnt += 1
                self.change_direction(self.direction, matrix[self.x][self.y])
            elif matrix[self.x][self.y] > 5:
                for hole in worm_holes[matrix[self.x][self.y]]:
                    if hole[0] == self.x and hole[1] == self.y:
                        continue
                    else:
                        temp_x = hole[0]
                        temp_y = hole[1]
                else:
                    self.x = temp_x
                    self.y = temp_y
        return cnt

    def go(self):
        if self.direction == 0:
            new_x = self.x
            new_y = self.y + 1
        elif self.direction == 1:
            new_x = self.x + 1
            new_y = self.y
        elif self.direction == 2:
            new_x = self.x
            new_y = self.y - 1
        elif self.direction == 3:
            new_x = self.x - 1
            new_y = self.y

        self.x = new_x
        self.y = new_y

    def change_direction(self, d, block):
        if d == 0:
            if block == 3:
                self.direction = 1
            elif block == 4:
                self.direction = 3
            else:
                self.direction = 2
        elif d == 1:
            if block == 1:
                self.direction = 0
            elif block == 4:
                self.direction = 2
            else:
                self.direction = 3
        elif d == 2:
            if block == 1:
                self.direction = 3
            elif block == 2:
                self.direction = 1
            else:
                self.direction = 0
        elif d == 3:
            if block == 2:
                self.direction = 0
            elif block == 3:
                self.direction = 2
            else:
                self.direction = 1


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [[-2]+list(map(int, input().split()))+[-2] for _ in range(N)]
    matrix.insert(0, [-2]*(N+2))
    matrix.append([-2]*(N+2))

    empty_space = []
    worm_holes = [False] * 11
    for i in range(1, N+2):
        for j in range(1, N+2):
            element = matrix[i][j]
            if element == 0:
                empty_space.append((i, j))
            elif element >= 6:
                if worm_holes[element]:
                    worm_holes[element].append((i, j))
                else:
                    worm_holes[element] = [(i, j)]

    result = 0
    for i, j in empty_space:
        for k in range(4):
            p = Pinball(i, j, k)
            temp_result = p.game()

            if temp_result > result:
                result = temp_result

    print('#{} {}'.format(test_case, result))
