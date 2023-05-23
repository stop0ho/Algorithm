N = int(input())
board = [list(input()) for _ in range(N)]
    

def check(board):
    M = 0
    for i in range(N):
        row_cnt = 1
        col_cnt = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]:
                row_cnt += 1
            else:
                row_cnt = 1
            if M < row_cnt:
                M = row_cnt
        
        for j in range(1, N):
            if board[j-1][i] == board[j][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            if M < col_cnt:
                M = col_cnt
    return M

ans = 0
for i in range(N):
    for j in range(N):
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            temp = check(board)
            if ans < temp:
                ans = temp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            temp = check(board)
            if ans < temp:
                ans = temp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)
