from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      targetY = i
      targetX = j
      result[i][j] = 0
    elif graph[i][j] == 0:
      result[i][j] = 0

q = deque([(targetY, targetX)])

while q:
  y, x = q.popleft()

  for k in range(4):
    newY = y + dy[k]
    newX = x + dx[k]

    if 0 <= newX < m and 0 <= newY < n and graph[newY][newX] == 1:
      result[newY][newX] = result[y][x] + 1
      q.append((newY, newX))
      graph[newY][newX] = 0

for i in result:
  print(*i)
