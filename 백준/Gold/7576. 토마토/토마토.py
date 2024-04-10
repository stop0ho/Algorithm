from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
q = deque()

# 처음에 받은 토마토 위치
for i in range(N):
  for j in range(M):
    if board[i][j] == 1:
      q.append([i, j])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
  y, x = q.popleft()
  for k in range(4):
    ny, nx = y + dy[k], x + dx[k]
    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
      board[ny][nx] = board[y][x] + 1
      q.append([ny, nx])

for l in board:
  for t in l:
    if t == 0:
      print(-1)
      exit(0)
  ans = max(ans, max(l))

print(ans - 1)