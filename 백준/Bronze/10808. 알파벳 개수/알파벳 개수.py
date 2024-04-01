alpa = input()
count = [0] * 26
for c in alpa:
  count[ord(c) - 97] += 1

print(*count)
