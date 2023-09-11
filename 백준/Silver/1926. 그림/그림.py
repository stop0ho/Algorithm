import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0 # 그림의 개수
area = 0 # 넓이

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j):
  global temp
  graph[i][j] = 0
  temp += 1

  for k in range(4):
    newX = dx[k] + j
    newY = dy[k] + i
    if 0 <= newX < m and 0 <= newY < n and graph[newY][newX]:
      dfs(newY, newX)


for i in range(n):
  for j in range(m):
    if graph[i][j]:
      temp = 0
      dfs(i, j)
      if temp > area:
        area = temp
      cnt += 1

print(cnt)
print(area)