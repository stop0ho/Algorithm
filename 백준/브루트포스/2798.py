from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_num = 0

for c in combinations(cards, 3):
    if max_num < sum(c) <= m:
        max_num = sum(c)

print(max_num)