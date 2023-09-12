import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
board = [[1]*n for _ in range(m)]
for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      board[i][j] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j):
  global temp
  temp += 1

  board[i][j] = 0

  for k in range(4):
    newX = dx[k] + j
    newY = dy[k] + i
    if 0 <= newX < n and 0 <= newY < m and board[newY][newX]:
      dfs(newY, newX)


cnt = 0
area = []
for i in range(m):
  for j in range(n):
    if board[i][j]:
      temp = 0
      dfs(i, j)
      area.append(temp)
      cnt += 1

print(cnt)
area.sort()
print(*area)