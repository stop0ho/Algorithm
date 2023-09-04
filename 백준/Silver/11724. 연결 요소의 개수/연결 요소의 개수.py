n, m = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
result = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = True

def dfs(idx):
  visited[idx] = True
  for i in range(1, n+1):
    if not visited[i] and graph[idx][i]:
      dfs(i)

for i in range(1, n+1):
  if not visited[i]:
    dfs(i)
    result += 1

print(result)