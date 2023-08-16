cow = {}
n = int(input())
ans = 0
for _ in range(n):
    num, now = map(int, input().split())
    if num in cow:
        if cow[num] != now:
            ans += 1
    cow[num] = now

print(ans)
