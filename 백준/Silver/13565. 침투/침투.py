import sys
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
answer = 'NO'
graph = [list(map(int, input())) for _ in range(m)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(row, col):
  graph[row][col] = 1
  global answer
  for k in range(4):
    y = row + dy[k]
    x = col + dx[k]
    if 0 <= x < n and 0 <= y < m and graph[y][x] == 0:
      if y == 0:
        answer = 'YES'
        return
      dfs(y, x)

for i in range(n):
  if graph[m-1][i] == 0:
    dfs(m-1, i)

print(answer)