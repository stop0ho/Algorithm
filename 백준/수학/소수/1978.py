N = int(input())

def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

nums = list(map(int, input().split()))
ans = 0
for x in nums:
    if prime(x):
        ans += 1

print(ans)