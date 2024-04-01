# 6, 9는 뒤집어서 쓸 수 있다.
count = [0] * 10
n = int(input())

while n:
  count[n % 10] += 1
  n //= 10

count[6] = (count[6] + count[9] + 1) // 2
count[9] = 0
print(max(count))