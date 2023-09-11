import sys
sys.setrecursionlimit(10**6)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

M = max(map(max, board))
m = min(map(min, board))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j, h):
  visited[i][j] = True
  
  for k in range(4):
    newX = dx[k] + j
    newY = dy[k] + i
    if 0 <= newX < n and 0 <= newY < n and not visited[newY][newX] and board[newY][newX] > h:
      dfs(newY, newX, h)
  
answer = 1

for height in range(m, M):
  visited = [[False] * n for _ in range(n)]
  temp = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j] and board[i][j] > height:
        dfs(i, j, height)
        temp += 1
  if answer < temp:
    answer = temp
  
print(answer)