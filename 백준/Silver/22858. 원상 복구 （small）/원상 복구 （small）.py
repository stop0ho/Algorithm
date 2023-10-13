# Di번째 카드를 i번째로 가져오는 것이 셔플
# 반대로 가야함 i번째거 Di번으로 보내야.
n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(k):
  temp_list = [0] * n
  for idx, num in enumerate(d):
    temp_list[num-1] = s[idx]
  s = temp_list

print(*s)