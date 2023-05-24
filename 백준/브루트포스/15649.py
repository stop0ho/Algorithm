'''
import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
nPr = list(itertools.permutations(nums, m))
l = len(nPr[0])
for i in nPr:
    for j in range(l):
        print(i[j], end=' ')
    print()
'''
c = [False] * 10
a = [] # 수열 저장
def go(index, n, m):
    # index번재의 수를 결정
    if index == m:
        return
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, n, m)
        c[i] = False

