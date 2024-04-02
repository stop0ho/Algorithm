t = int(input())

for _ in range(t):
  sl = []
  sr = []
  pw = input()
  for i in pw:
    if i == '-':
      if sl:
        sl.pop()
    elif i == '<':
      if sl:
        sr.append(sl.pop())
    elif i == '>':
      if sr:
        sl.append(sr.pop())
    else:
      sl.append(i)
  sl.extend(reversed(sr))
  print(''.join(sl))