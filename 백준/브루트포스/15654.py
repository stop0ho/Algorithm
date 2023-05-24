from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nPm = list(permutations(nums, m))
nPm.sort()

for i in nPm:
    for j in range(m):
        print(i[j], end = ' ')
    print()


