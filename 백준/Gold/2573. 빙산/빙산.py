from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


# 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어듦
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 섬 개수
def bfs(i, j):
  q = deque([[i, j]])
  visited[i][j] = True

  while q:
    y, x = q.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board[ny][nx]:
        visited[ny][nx] = True
        q.append([ny, nx])

# 무조건 한 덩어리의 빙산 주어진다 했으니까 최소 한 번은 돌아야 함.
ans = 0

while True:
  # 1년 뒤 녹는 것
  ans += 1
  minus = deque()
  for i in range(N):
    for j in range(M):
      if board[i][j] > 0:
        cnt = 0
        for k in range(4):
          ny = dy[k] + i
          nx = dx[k] + j
          if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == 0:
              cnt += 1
        minus.append([i, j, cnt])
  
  if len(minus) == 0:
    print(0)
    break
  
  while minus:
    i, j, cnt = minus.pop()
    board[i][j] -= cnt
    # 각 칸에 저장된 높이는 0보다 더 줄어들지 않음
    if board[i][j] < 0:
      board[i][j] = 0

  island = 0
  visited = [[False] * M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if board[i][j] and not visited[i][j]:
          if island == 0:
            island += 1
            bfs(i, j)
          else:
            print(ans)
            exit()