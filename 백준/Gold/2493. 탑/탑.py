N = int(input())
T = list(map(int, input().split()))
ans = [0] * N
stack = []

for i in range(len(T)):
  while stack:
    if T[stack[-1][0]] < T[i]:
      stack.pop()
    else:
      ans[i] = stack[-1][0] + 1
      break
  stack.append((i, T[i]))

print(*ans)