from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nCm = [list(i) for i in combinations(nums, m)]
nCm = [sorted(i) for i in nCm]
nCm.sort()

for i in nCm:
    for j in range(m):
        print(i[j], end = ' ')
    print()