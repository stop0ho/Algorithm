n = int(input())
target = int(input())
snail = [[0] * n for _ in range(n)]

x = n//2
y = n//2
snail[x][y] = 1

num = 2
s = 3

# 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def go(g):
    global x, y, snail, num
    x += dx[g]
    y += dy[g]
    snail[y][x] = num
    num += 1


while s <= n:
    go(0)
    for _ in range(s-2):
        go(1)
    for _ in range(s-1):
        go(2)
    for _ in range(s-1):
        go(3)
    for _ in range(s-1):
        go(0)
    s += 2

for i in range(n):
    print(*snail[i])
    if target in snail[i]:
        rx = i + 1
        ry = snail[i].index(target) + 1

print(rx, ry)
