n = int(input())
start, end = map(int, input().split())
m = int(input())
answer = -1

visited = [False] * (n+1)

# graph 채우기
graph = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True

def dfs(idx, count):
  global answer
  visited[idx] = True
  if (idx == end):
    answer = count
    return
  
  for i in range(1, n+1):
    if not visited[i] and graph[idx][i]:
      dfs(i, count + 1)

dfs(start, 0)
print(answer)