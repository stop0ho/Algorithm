n = int(input())
m = int(input())
answer = 0

visited = [False] * (n+1)

# graph 채우기
graph = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True


def dfs(idx):
  global answer
  answer += 1
  visited[idx] = True
  for i in range(1, n+1):
    if not visited[i] and graph[idx][i]:
      dfs(i)

dfs(1)
print(answer - 1)