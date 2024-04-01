number = 1

for _ in range(3):
  number *= int(input())

numbers = list(str(number))
for i in range(10):
  print(numbers.count(str(i)))
