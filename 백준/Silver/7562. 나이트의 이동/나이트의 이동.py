from collections import deque

T = int(input())
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(T):
  l = int(input())
  board = [[-1] * l for _ in range(l)]
  ny, nx = map(int, input().split())
  ty, tx = map(int, input().split())
  board[ny][nx] = 0
  q = deque([[ny, nx]])
  while q:
    y, x = q.popleft()
    if y == ty and x == tx:
      print(board[y][x])
      break
    for k in range(8):
      newY = y + dy[k]
      newX = x + dx[k]
      if 0 <= newY < l and 0 <= newX < l and board[newY][newX] == -1:
        board[newY][newX] = board[y][x] + 1
        q.append([newY, newX])
