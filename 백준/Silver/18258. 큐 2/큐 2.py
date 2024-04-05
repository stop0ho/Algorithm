from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
q = deque()

for _ in range(N):
  ins = input().split()
  if ins[0] == 'push':
    q.append(ins[1])
  elif ins[0] == 'pop':
    if not q:
      print(-1)
      continue
    print(q.popleft())
  elif ins[0] == 'size':
    print(len(q))
  elif ins[0] == 'empty':
    if q:
      print(0)
    else:
      print(1)
  elif ins[0] == 'front':
    if not q:
      print(-1)
      continue
    print(q[0])
  elif ins[0] == 'back':
    if not q:
      print(-1)
      continue
    print(q[-1])