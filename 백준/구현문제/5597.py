numbers = {i:False for i in range(1, 31)}

for _ in range(28):
    n = int(input())
    numbers[n] = True

for num in numbers:
    if not numbers[num]:
        print(num)
