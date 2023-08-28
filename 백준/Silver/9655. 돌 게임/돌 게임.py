n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = i//3 + i%3

if dp[n] % 2 == 1:
    print('SK')
else:
    print('CY')
