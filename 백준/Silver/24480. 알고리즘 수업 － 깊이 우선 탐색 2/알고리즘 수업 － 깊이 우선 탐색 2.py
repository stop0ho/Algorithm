import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort(reverse=True)

cnt = 1
def dfs(idx):
    global cnt
    visited[idx] = cnt
    cnt += 1

    for i in graph[idx]:
        if visited[i] == 0:
            dfs(i)
dfs(R)
for i in range(1, N+1):
    print(visited[i])
