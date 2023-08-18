import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            target = board[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == target:
                    cnt += 1
                    if cnt == 5:
                        # 그 다음게 같은지 확인
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == target:
                            break
                        # 이전에 같은 게 있었을지 확인
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == target:
                            break
                        # break되지 않으면 5개만 있는것임
                        print(target)
                        print(x + 1, y + 1)
                        sys.exit(0)
                    nx += dx[i]
                    ny += dy[i]

print(0)