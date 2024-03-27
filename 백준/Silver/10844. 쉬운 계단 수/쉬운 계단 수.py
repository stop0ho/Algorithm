n = int(input())
dp = [[0] * 10 for _ in range(n+1)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
  dp[i][0] = dp[i-1][1] # 0의 앞에는 1만 올 수 있음
  dp[i][9] = dp[i-1][8] # 9의 앞에는 8만 올 수 있음
  for j in range(1, 9):
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)
