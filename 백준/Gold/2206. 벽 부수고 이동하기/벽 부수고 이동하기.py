from collections import deque

# 시작하는 칸과 끝나는 칸 포함해서 셈 => 거리 1에서 시작
# 벽을 최대 한 개 부수고 이동할 수 있음
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 인덱스 0 : 벽을 안 부순 경로
# 인덱스 1 : 벽을 부순 경로
dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs(x, y):
  q = deque([[x, y, 0]])
  dist[y][x][0] = 1

  while q:
    a, b, c = q.popleft()
    if a == M - 1 and b == N - 1:
      return dist[b][a][c]
    
    for k in range(4):
      nx, ny = a+dx[k], b+dy[k]
      if 0 <= nx < M and 0 <= ny < N:
        if graph[ny][nx] == 1 and c == 0:
          dist[ny][nx][1] = dist[b][a][0] + 1
          q.append([nx, ny, 1])
        if graph[ny][nx] == 0 and dist[ny][nx][c] == 0:
          dist[ny][nx][c] = dist[b][a][c] + 1
          q.append([nx, ny, c])
  return -1

print(bfs(0, 0))