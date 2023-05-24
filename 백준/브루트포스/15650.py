import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
nCr = list(itertools.combinations(nums, m))
l = len(nCr[0])
for i in nCr:
    for j in range(l):
        print(i[j], end=' ')
    print()