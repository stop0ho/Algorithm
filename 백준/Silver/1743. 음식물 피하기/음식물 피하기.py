import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
  global cnt
  cnt += 1

  board[y][x] = 0

  for k in range(4):
    newY = dy[k] + y
    newX = dx[k] + x
    if 0 <= newY < n and 0 <= newX < m and board[newY][newX] == 1:
      dfs(newY, newX)
      

for _ in range(k):
  r, c = map(int, input().split())
  board[r-1][c-1] = 1

for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      cnt = 0
      dfs(i, j)
      if cnt > answer: answer = cnt

print(answer)
