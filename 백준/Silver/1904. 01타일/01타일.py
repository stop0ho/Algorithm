# 00 타일 / 1 타일. 이렇게 두 가지 사용 가능
# N=1 : 1 (1)
# N=2 : 11, 00 (2)
# N=3 : 001, 100, 111 (3)
# N=4 : 0011, 0000, 1001, 1100, 1111 (5)
n = int(input())
dp = [0, 1, 2]

for i in range(3, n+1):
  dp.append((dp[i-1] + dp[i-2])%15746)

print(dp[n])

