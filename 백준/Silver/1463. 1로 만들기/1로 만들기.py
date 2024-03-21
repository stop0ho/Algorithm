from collections import deque

x = int(input())

dp = deque([x])
result = -1
flag = False

while not flag:
  for _ in range(len(dp)):
    n = dp.popleft()
    if n == 1:
      flag = True
      break
    if n % 3 == 0:
      dp.append(n//3)
    if n % 2 == 0:
      dp.append(n//2)
    dp.append(n-1)
  result += 1

print(result)