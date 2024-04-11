from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

fire_board = [[-1] * C for _ in range(R)]
jihun_board = [[-1] * C for _ in range(C)]
ans = 0
flag = False

fire = deque()
jihun = deque()
for i in range(R):
  for j in range(C):
    if board[i][j] == 'F':
      fire.append([i, j])
      fire_board[i][j] = 1
    if board[i][j] == 'J':
      jihun.append([i, j])
      jihun_board[i][j] = 1


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while fire:
  y, x = fire.popleft()
  for k in range(4):
    newY = y + dy[k]
    newX = x + dx[k]
    if 0 <= newY < R and 0 <= newX < C:
      if fire_board[newY][newX] == -1 and board[newY][newX] != '#':
        fire_board[newY][newX] = fire_board[y][x] + 1
        fire.append([newY, newX])

while jihun and not flag:
  y, x = jihun.popleft()
  for k in range(4):
    newY = y + dy[k]
    newX = x + dx[k]
    if 0 <= newY < R and 0 <= newX < C:
      if board[newY][newX] != '#' and jihun_board[newY][newX] == -1:
        if fire_board[newY][newX] == -1 or fire_board[newY][newX] > jihun_board[y][x]+1:
          jihun_board[newY][newX] = jihun_board[y][x] + 1
          jihun.append([newY, newX])
    else:
      print(jihun_board[y][x])
      flag = True
      break


if not flag:
  print('IMPOSSIBLE')
