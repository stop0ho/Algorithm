n, m = map(int, input().split())
dna = []
for _ in range(n):
    d = input()
    dna.append(d)

ans = ''
sum = 0

for c in zip(*dna):
    cnt = {d: 0 for d in 'ACGT'}
    for k in c:
        cnt[k] += 1
    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    ans += cnt[0][0]
    sum += (n - cnt[0][1])

print(ans)
print(sum)