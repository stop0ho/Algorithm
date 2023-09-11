n = int(input())
board = [list(input()) for _ in range(n)]
groupCnt = 0
result = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
  global cnt
  cnt += 1
  board[y][x] = '0'

  for k in range(4):
    newY = y + dy[k]
    newX = x + dx[k]
    if 0 <= newX < n and 0 <= newY < n and board[newY][newX] == '1':
      dfs(newY, newX)

for i in range(n):
  for j in range(n):
    if board[i][j] == '1':
      cnt = 0
      dfs(i, j)
      result.append(cnt)
      groupCnt += 1

print(groupCnt)
result.sort()
for i in result:
  print(i)