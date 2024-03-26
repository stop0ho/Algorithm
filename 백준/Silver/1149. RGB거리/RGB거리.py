# 1번 != 2번
# N번 != N-1번
# i(2 <= i <= N-1)번 != i-1, i+1

n = int(input())
rgb_list = []
dp = [[0] * 3 for _ in range(n)]
for _ in range(n):
  rgb_list.append(list(map(int, input().split())))

dp[0][0], dp[0][1], dp[0][2] = rgb_list[0][0], rgb_list[0][1], rgb_list[0][2]

for i in range(1, n):
  dp[i][0] = min(dp[i-1][1] + rgb_list[i][0], dp[i-1][2] + rgb_list[i][0])
  dp[i][1] = min(dp[i-1][0] + rgb_list[i][1], dp[i-1][2] + rgb_list[i][1])
  dp[i][2] = min(dp[i-1][0] + rgb_list[i][2], dp[i-1][1] + rgb_list[i][2])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))