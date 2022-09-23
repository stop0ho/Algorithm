# 1940 문제와 비슷하지만 본인을 제외한 수로 해야한다는 것에 유의

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

count = 0

for i in range(n):
    find = A[i]
    s = 0
    e = n - 1
    while s < e:
        if A[s] + A[e] == find:
            if e != i and s != i:
                count += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
        elif A[s] + A[e] < find:
            s += 1
        elif A[s] + A[e] > find:
            e -= 1
        
print(count)