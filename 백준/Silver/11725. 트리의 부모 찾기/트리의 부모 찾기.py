from collections import deque
import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [deque() for _ in range(n+1)]
checked = [False] * (n+1)
parent = [0] * (n+1)
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(idx):
  checked[idx] = True
  while graph[idx]:
    i = graph[idx].popleft()
    if not checked[i]:
      parent[i] = idx
      dfs(i)

dfs(1)

for i in range(2, n+1):
  print(parent[i])

