import sys
sys.setrecursionlimit(10**6)

# 상하좌우 대각선
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def dfs(row, col):
  board[row][col] = 0

  for k in range(8):
    y = dy[k] + row
    x = dx[k] + col
    if 0 <= x < w and 0 <= y < h and board[y][x] == 1:
      dfs(y, x)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  board = [list(map(int, input().split())) for _ in range(h)]
  answer = 0
  for i in range(h):
    for j in range(w):
      if board[i][j] == 1:
        dfs(i, j)
        answer += 1
  print(answer)
