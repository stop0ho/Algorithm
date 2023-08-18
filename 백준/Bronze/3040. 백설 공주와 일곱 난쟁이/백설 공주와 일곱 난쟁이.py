from itertools import combinations

humans = [int(input()) for _ in range(9)]
comb = list(combinations(humans, 7))
for com in comb:
  if sum(com) == 100:
    for hum in com:
      print(hum)