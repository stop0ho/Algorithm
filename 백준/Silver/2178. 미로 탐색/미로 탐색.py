from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque([(0, 0)])

while q:
  i, j = q.popleft()

  for k in range(4):
    ni = i + dy[k]
    nj = j + dx[k]

    if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 1:
      q.append((ni, nj))
      graph[ni][nj] = graph[i][j] + 1

print(graph[n-1][m-1])