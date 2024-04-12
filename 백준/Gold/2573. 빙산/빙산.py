from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def melting(icebergs, n, m):
    new_icebergs = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if icebergs[i][j] > 0:
                count = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if check(ni, nj, n, m) and icebergs[ni][nj] == 0:
                        count += 1
                new_icebergs[i][j] = max(icebergs[i][j] - count, 0)
    return new_icebergs

def bfs(icebergs, visited, start, n, m):
    q = deque([start])
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny, n, m) and icebergs[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

def count_islands(icebergs, n, m):
    islands = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if icebergs[i][j] > 0 and not visited[i][j]:
                bfs(icebergs, visited, (i, j), n, m)
                islands += 1

    return islands

def main():
    n, m = map(int, input().split())
    icebergs = [list(map(int, input().split())) for _ in range(n)]
    
    years = 0
    while True:
        islands = count_islands(icebergs, n, m)
        
        if islands == 0:
            print(0)
            return
        
        if islands >= 2:
            print(years)
            return
        
        icebergs = melting(icebergs, n, m)
        years += 1

if __name__ == "__main__":
    main()