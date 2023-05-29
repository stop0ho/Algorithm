n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(px, py, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            if c[x][y]:
                continue
            ok = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if c[nx][ny]:
                        ok = False
                if ok:
                    c[x][y] = True
                    go(x, y, cnt+1, s+a[x][y])
                    c[x][y] = False

go(0, 0, 0, 0)
print(ans)