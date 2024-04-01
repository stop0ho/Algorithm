n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
answer = 0

numbers.sort()
i = 0
j = n-1
while i < j:
  if numbers[i] + numbers[j] == x:
    answer += 1
    i += 1
    j -= 1
  elif numbers[i] + numbers[j] < x:
    i += 1
  else:
    j -= 1

print(answer)