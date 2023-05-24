import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
nHr = list(itertools.product(nums, repeat = m))
for i in nHr:
    for j in range(m):
        print(i[j], end=' ')
    print()