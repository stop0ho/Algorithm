n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 'Hing'

def dfs(x, y):
  if board[y][x] == -1:
    global answer
    answer = 'HaruHaru'
  dx = x + board[y][x]
  dy = y + board[y][x]
  board[y][x] = 0
  if 0 <= dx < n and board[y][dx] != 0:
    dfs(dx, y)
  if 0 <= dy < n and board[dy][x] != 0:
    dfs(x, dy)

dfs(0, 0)
print(answer)