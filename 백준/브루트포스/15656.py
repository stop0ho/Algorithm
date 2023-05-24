from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nPm = [list(i) for i in combinations_with_replacement(nums, m)]

for i in nPm:
    for j in range(m):
        print(i[j], end = ' ')
    print()