n = int(input())
vol = [0] * 10000
dp = [0] * 10000

for i in range(n):
  vol[i] = int(input())

dp[0] = vol[0]
dp[1] = vol[0] + vol[1]
dp[2] = max(vol[2] + vol[0], vol[2] + vol[1], dp[1])

for i in range(3, n):
  dp[i] = max(vol[i] + vol[i-1] + dp[i-3], vol[i] + dp[i-2], dp[i-1])

print(max(dp))