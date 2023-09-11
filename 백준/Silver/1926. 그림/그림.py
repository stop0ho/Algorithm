from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0 # 그림의 개수
area = 0 # 넓이

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
  global temp
  q = [(i, j)]
  graph[i][j] = 0
  while q:
    ey, ex = q.pop()
    for k in range(4):
      newY = dy[k] + ey
      newX = dx[k] + ex
      if 0 <= newX < m and 0 <= newY < n and graph[newY][newX]:
        q.append((newY, newX))
        graph[newY][newX] = 0
        temp += 1


for i in range(n):
  for j in range(m):
    if graph[i][j]:
      temp = 1
      bfs(i, j)
      if temp > area:
        area = temp
      cnt += 1

print(cnt)
print(area)