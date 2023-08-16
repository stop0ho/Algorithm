N = int(input())
for i in range(1, 1000001):
    sum = i
    for c in str(i):
        sum += int(c)
    if sum == N:
        print(i)
        break
else:
    print(0)
