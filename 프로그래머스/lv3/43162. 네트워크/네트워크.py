from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    
    def bfs(v):
        q = deque([v])
        visited[v] = True
        
        while q:
            num = q.popleft()
            for i in graph[num]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i+1].append(j+1)
    
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            answer += 1
                
    return answer