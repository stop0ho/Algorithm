from collections import deque

N = int(input())
board = [list(input()) for _ in range(N)]
visit1 = [[False] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()
ans1 = 0
ans2 = 0

for i in range(N):
  for j in range(N):
    if not visit1[i][j]:
      q.append([i, j])
      ans1 += 1
      target = board[i][j]
      visit1[i][j] = True
      while q:
        y, x = q.popleft()
        for k in range(4):
          ny = y + dy[k]
          nx = x + dx[k]
          if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == target and not visit1[ny][nx]:
            visit1[ny][nx] = True
            q.append([ny, nx])

for i in range(N):
  for j in range(N):
    if board[i][j]:
      q.append([i, j])
      ans2 += 1
      target = board[i][j]
      board[i][j] = ''
      while q:
        y, x = q.popleft()
        for k in range(4):
          ny = y + dy[k]
          nx = x + dx[k]
          if 0 <= ny < N and 0 <= nx < N:
            if target in ['R', 'G']:
              if board[ny][nx] in ['R', 'G']:
                board[ny][nx] = ''
                q.append([ny, nx])
            else:
              if board[ny][nx] == target:
                board[ny][nx] = ''
                q.append([ny, nx])
      
print(ans1, ans2)