from collections import deque

N, K = map(int, input().split())
MAX = 1000001
graph = [0] * 1000001

q = deque([N])

while q:
  dis = q.pop()
  if dis == K:
    print(graph[K])
    break
  for i in (dis+1, dis-1, dis*2):
    if 0 <= i < MAX and not graph[i]:
      graph[i] = graph[dis] + 1
      q.appendleft(i)

