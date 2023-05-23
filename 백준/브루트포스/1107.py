N = int(input())
M = int(input())
broken = [False] * 10
if M > 0:
    for i in map(int, input().split()):
        broken[i] = True


def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l

ans = abs(N - 100) # 숫자버튼을 안 누른 경우

for i in range(0, 1000001):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-N)
        if ans > l + press:
            ans = l + press

print(ans)