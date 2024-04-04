K = int(input())
numbers = []

for _ in range(K):
  num = int(input())
  if num == 0:
    numbers.pop()
    continue
  numbers.append(num)

print(sum(numbers))