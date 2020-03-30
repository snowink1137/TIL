import sys

sys.stdin = open('17143.txt', 'r')


class Shark:
    def __init__(self, x, y, s, d, z):
        self.x = x
        self.y = y
        self.s = s
        self.d = d
        self.z = z

    def move(self):
        temp_s = self.s
        while temp_s > 0:
            if self.d == 1:
                if self.x == 0:
                    self.d = 2
                else:
                    self.x -= 1
                    temp_s -= 1
            elif self.d == 2:
                if self.x == R-1:
                    self.d = 1
                else:
                    self.x += 1
                    temp_s -= 1
            elif self.d == 3:
                if self.y == C-1:
                    self.d = 4
                else:
                    self.y += 1
                    temp_s -= 1
            else:
                if self.y == 0:
                    self.d = 3
                else:
                    self.y -= 1
                    temp_s -= 1

        if new_grid[self.x][self.y]:
            if self.z > new_grid[self.x][self.y].z:
                new_objects.remove(new_grid[self.x][self.y])
                new_grid[self.x][self.y] = self
                new_objects.append(self)
        else:
            new_grid[self.x][self.y] = self
            new_objects.append(self)


R, C, M = map(int, input().split())
grid = [[False for _ in range(C)] for _ in range(R)]
objects = []

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    temp = Shark(r-1, c-1, s, d, z)
    grid[r-1][c-1] = temp
    objects.append(temp)

result = 0
for j in range(C):
    new_grid = [[False for _ in range(C)] for _ in range(R)]
    new_objects = []

    for i in range(R):
        if grid[i][j]:
            result += grid[i][j].z
            objects.remove(grid[i][j])
            break

    for obj in objects:
        obj.move()

    grid = [row[:] for row in new_grid[:]]
    objects = new_objects[:]

print(result)
