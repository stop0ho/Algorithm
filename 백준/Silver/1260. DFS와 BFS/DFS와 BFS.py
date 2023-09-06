from collections import deque

dfs_result = []
bfs_result = []

n, m, v = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(idx):
  visited[idx] = True
  dfs_result.append(idx)
  for i in range(1, n+1):
    if not visited[i] and i in graph[idx]:
      dfs(i)

def bfs():
  # 초기화 작업
  q = deque()
  visited = [False] * (n+1)

  q.append(v)
  visited[v] = True
  
  while (len(q) != 0):
    idx = q.popleft()
    bfs_result.append(idx)

    for i in range(1, n+1):
      if not visited[i] and i in graph[idx]:
        q.append(i)
        visited[i] = True

dfs(v)
bfs()
print(*dfs_result)
print(*bfs_result)