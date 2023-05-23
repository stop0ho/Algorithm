n, m = map(int, input().split())
p = []
for _ in range(n):
    pl = list(map(int, input().split()))
    p.append(pl)

ans = 0
for i in range(n):
    for j in range(m):
        # 테트로미노 1
        if j < m - 3:
            temp = p[i][j] + p[i][j+1] + p[i][j+2] + p[i][j+3]
            if ans < temp:
                ans = temp
        if i < n - 3:
            temp = p[i][j] + p[i+1][j] + p[i+2][j] + p[i+3][j]
            if ans < temp:
                ans = temp
        
        # 테트로미노 2
        if j < m - 1 and i < n - 1:
            temp = p[i][j] + p[i+1][j] + p[i][j+1] + p[i+1][j+1]
            if ans < temp:
                ans = temp
        
        # 테트로미노 3
        if j < m - 2 and i < n - 1:
            temp = p[i][j] + p[i][j+1] + p[i][j+2] + p[i+1][j+1]
            if ans < temp:
                ans = temp
        if j < m - 2 and i < n - 1:
            temp = p[i][j+1] + p[i+1][j] + p[i+1][j+1] + p[i+1][j+2]
            if ans < temp:
                ans = temp
        if j < m - 1 and i < n - 2:
            temp = p[i][j] + p[i+1][j] + p[i+1][j+1] + p[i+2][j]
            if ans < temp:
                ans = temp
        if j < m - 1 and i < n - 2:
            temp = p[i][j+1] + p[i+1][j] + p[i+1][j+1] + p[i+2][j+1]
            if ans < temp:
                ans = temp

        # 테트로미노 4
        if j < m-1 and i < n-2:
            temp = p[i][j] + p[i+1][j] + p[i+1][j+1] + p[i+2][j+1]
            if ans < temp:
                ans = temp
        if j < m-1 and i < n-2:
            temp = p[i][j+1] + p[i+1][j] + p[i+1][j+1] + p[i+2][j]
            if ans < temp:
                ans = temp
        if i < n - 1 and j < m - 2:
            temp = p[i][j+1] + p[i][j+2] + p[i+1][j] + p[i+1][j+1]
            if ans < temp:
                ans = temp
        if i < n - 1 and j < m - 2:
            temp = p[i][j] + p[i][j+1] + p[i+1][j+1] + p[i+1][j+2]
            if ans < temp:
                ans = temp
        
        # 테트로미노 5
        if i < n - 2 and j < m - 1:
            temp = p[i][j] + p[i+1][j] + p[i+2][j] + p[i+2][j+1]
            if ans < temp:
                ans = temp
        if i < n - 2 and j < m - 1:
            temp = p[i][j] + p[i+1][j] + p[i+2][j] + p[i+1][j+1]
            if ans < temp:
                ans = temp
        if i < n - 2 and j < m - 1:
            temp = p[i][j+1] + p[i+1][j+1] + p[i+2][j+1] + p[i+2][j]
            if ans < temp:
                ans = temp
        if i < n - 2 and j < m - 1:
            temp = p[i][j] + p[i][j+1] + p[i+1][j+1] + p[i+2][j+1]
            if ans < temp:
                ans = temp

        if i < n - 1 and j < m - 2:
            temp = p[i][j] + p[i][j+1] + p[i][j+2] + p[i+1][j]
            if ans < temp:
                ans = temp
        if i < n - 1 and j < m - 2:
            temp = p[i][j] + p[i][j+1] + p[i][j+2] + p[i+1][j+1]
            if ans < temp:
                ans = temp
        if i < n - 1 and j < m - 2:
            temp = p[i][j] + p[i+1][j] + p[i+1][j+1] + p[i+1][j+2]
            if ans < temp:
                ans = temp
        if i < n - 1 and j < m - 2:
            temp = p[i][j+2] + p[i+1][j] + p[i+1][j+1] + p[i+1][j+2]
            if ans < temp:
                ans = temp

print(ans)