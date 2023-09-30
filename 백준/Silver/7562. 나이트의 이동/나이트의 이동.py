from collections import deque

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(int(input())):
  l = int(input())
  r1, c1 = map(int, input().split())
  r2, c2 = map(int, input().split())
  graph = [[0] * l for _ in range(l)]
  visited = [[False] * l for _ in range(l)]
  q = deque([(r1, c1)])
  visited[r1][c1] = True
  while q:
      y, x = q.popleft()
      if y == r2 and x == c2:
        print(graph[r2][c2])
        break
      for k in range(8):
        newY = y + dy[k]
        newX = x + dx[k]
        if 0 <= newY < l and 0 <= newX < l and not visited[newY][newX]:
          q.append((newY, newX))
          graph[newY][newX] = graph[y][x] + 1
          visited[newY][newX] = True
