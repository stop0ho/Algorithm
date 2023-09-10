n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = 0

def dfs(y, x, cnt):
  # 방문한 곳 처리
  board[y][x] = ''
  if cnt == '-':
    dx = x+1
    dy = y
  elif cnt == '|':
    dx = x
    dy = y+1
  
  if 0 <= dx < m and 0 <= dy < n and board[dy][dx] == cnt:
    dfs(dy, dx, cnt)

for i in range(n):
  for j in range(m):
    if board[i][j]:
      dfs(i, j, board[i][j])
      answer += 1

print(answer)
