h, w = map(int, input().split())
n = int(input())

grid = [[0]*w for _ in range(h)]

for _ in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(l):
        if d == 0:
            grid[x][y + i] = 1
        else:
            grid[x + i][y] = 1

for row in grid:
    print(" ".join(map(str, row)))
