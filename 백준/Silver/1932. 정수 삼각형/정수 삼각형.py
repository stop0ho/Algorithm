n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = triangle[0][0] # 맨 위의 값은 하나만 있으므로
for i in range(0, n-1):
    for j in range(0, i+1):
        if dp[i+1][j] < dp[i][j] + triangle[i+1][j]: # 왼쪽 채우기
            dp[i+1][j] = dp[i][j] + triangle[i+1][j]
        if dp[i+1][j+1] < dp[i][j] + triangle[i+1][j+1]: # 오른쪽 채우기
            dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]

print(max(dp[-1]))