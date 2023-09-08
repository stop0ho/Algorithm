import sys
sys.setrecursionlimit(10**6)

t = int(input())

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(row, col):
  board[row][col] = 0
  for i in range(4):
    y = row + dy[i]
    x = col + dx[i]
    if 0 <= x < M and 0 <= y < N and board[y][x] == 1:
      dfs(y, x)



for _ in range(t):
  M, N, K = map(int, input().split())
  board = [[0] * M for _ in range(N)]
  answer = 0

  # 그래프 채우기
  for _ in range(K):
    a, b = map(int, input().split())
    board[b][a] = 1
  
  for i in range(N):
    for j in range(M):
      if board[i][j] == 1:
        dfs(i, j)
        answer += 1
  print(answer)
