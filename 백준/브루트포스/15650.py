import sys
n, m = map(int, input().split())

check = [False] * (n+1)
ans = [0] * m

# index번째의 수열 결정하는 함수
def P(n, m, index, start):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(start, n+1):
        if check[i]:
            continue
        check[i] = True
        ans[index] = i
        P(n, m, index+1, i+1)
        check[i] = False

P(n, m, 0, 1)

