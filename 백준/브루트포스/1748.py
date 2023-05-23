N = int(input())

ans = 0
start = 1
len = 1
while start <= N:
    end = start * 10 - 1
    if end > N:
        end = N
    ans += (end - start + 1) * len
    start *= 10
    len += 1

print(ans)
