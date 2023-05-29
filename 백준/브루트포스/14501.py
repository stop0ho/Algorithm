n = int(input())
T = []
P = []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

max = 0
def go(t, p, index, sum):
    if index == n:
        global max
        if max < sum:
            max = sum
        return
    if index > n:
        return
    go(t, p, index + t[index], sum + p[index])
    go(t, p, index+1, sum)
    
go(T, P, 0, 0)
print(max)