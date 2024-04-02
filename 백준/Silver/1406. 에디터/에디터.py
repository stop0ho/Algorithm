import sys
input = sys.stdin.readline

sl = list(input())
sl.pop()
n = int(input())
sr = []

for _ in range(n):
  cmd = input().split()

  if cmd[0] == 'L' and sl:
    sr.append(sl.pop())
  elif cmd[0] == 'D' and sr:
    sl.append(sr.pop())
  elif cmd[0] == 'B' and sl:
    sl.pop()
  elif cmd[0] == 'P':
    sl.append(cmd[1])

print(''.join(sl + list(reversed(sr))))