t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    
    if d < 0:
        d = 360 + d
    turn = d // 45
    if turn == 0:
        result = l
    before = [nums[:] for nums in l]
    for _ in range(turn):
        result = [nums[:] for nums in before]
        for i in range(n):
            result[i][n//2] = before[i][i]
            result[i][n-1-i] = before[i][n//2]
            result[n//2][n-1-i] = before[i][n-1-i]
            result[i][i] = before[n//2][i]
        before = [nums[:] for nums in result]
    
    for i in range(n):
        print(*result[i])