from itertools import combinations

nums = []
for _ in range(9):
    num = int(input())
    nums.append(num)

combi = list(combinations(nums, 7))
for i in combi:
    if sum(i) == 100:
        result = i
        
result = list(result)
result.sort()
for i in result:
    print(i)