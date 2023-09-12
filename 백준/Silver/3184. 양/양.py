import sys
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

sheep = 0
wolf = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j):
  global temp_sheep
  global temp_wolf

  if board[i][j] == 'v':
    temp_wolf += 1
  elif board[i][j] == 'o':
    temp_sheep += 1

  board[i][j] = '#'

  for k in range(4):
    newY = dy[k] + i
    newX = dx[k] + j
    if 0 <= newX < c and 0 <= newY < r and board[newY][newX] != '#':
      dfs(newY, newX)

for i in range(r):
  for j in range(c):
    if board[i][j] != '#':
      temp_sheep = 0
      temp_wolf = 0
      dfs(i, j)
      if temp_sheep > temp_wolf: sheep += temp_sheep
      else: wolf += temp_wolf

print(sheep, wolf)