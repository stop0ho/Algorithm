from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = []

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

def bfs():
  q = deque([(x, 0)])
  visited[x] = True
  
  while q:
    num, d = q.popleft()
    if d == k:
      answer.append(num)

    for i in graph[num]:
      if not visited[i]:
        q.append((i, d+1))
        visited[i] = True

bfs()
if not answer:
  print(-1)
else:
  answer.sort()
  for i in answer:
    print(i, end='\n')