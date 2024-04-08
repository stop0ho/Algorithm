from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())
for _ in range(n):
  op = input().split()
  if op[0] == 'push_front':
    dq.appendleft(op[1])
  elif op[0] == 'push_back':
    dq.append(op[1])
  elif op[0] == 'pop_front':
    if not dq:
      print(-1)
      continue
    print(dq.popleft())
  elif op[0] == 'pop_back':
    if not dq:
      print(-1)
      continue
    print(dq.pop())
  elif op[0] == 'size':
    print(len(dq))
  elif op[0] == 'empty':
    if dq:
      print(0)
    else:
      print(1)
  elif op[0] == 'front':
    if not dq:
      print(-1)
      continue
    print(dq[0])
  elif op[0] == 'back':
    if not dq:
      print(-1)
      continue
    print(dq[-1])