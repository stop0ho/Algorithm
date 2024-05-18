T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    row_c = 0
    col_c = 0
    
    for i in range(n):
        r_cnt = 0
        c_cnt = 0
        for j in range(n):
            # row_c 구하기
            if board[i][j] == 0:
                if r_cnt == k:
                    row_c += 1
                r_cnt = 0
            else:
                r_cnt += 1
            # col_c 구하기
            if board[j][i] == 0:
                if c_cnt == k:
                    col_c += 1
                c_cnt = 0
            else:
                c_cnt += 1
            if j == n-1:
                if board[j][i] == 1 and c_cnt == k:
                    col_c += 1
                if board[i][j] == 1 and r_cnt == k:
                    row_c += 1
    print('#%d %d' % (test_case, row_c + col_c))

                    
            
            
