from collections import deque

def solution(maps):
    q = deque([(0, 0)])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while q:
        i, j = q.popleft()
        
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] == 1:
                q.append((ni, nj))
                maps[ni][nj] = maps[i][j] + 1
    
    if maps[-1][-1] <= 1:
        return -1
    else:
        return maps[-1][-1]