board = [list(map(int, input().split())) for _ in range(19)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(19):
        board[x][i] = 1 - board[x][i] 
        board[i][y] = 1 - board[i][y] 
for row in board:
    print(' '.join(map(str, row)))