from collections import deque

T = int(input())

for _ in range(T):
  # p 작업
  p = input()
  dc = p.count('D')
  
  # 덱 작업
  n = int(input())
  l = input()
  l = l[1:-1]
  if n == 0:
    dq = deque()
  else:
    dq = deque(l.split(','))

  # 함수 수행
  if n < dc:
    print('error')
    continue
  
  rev = 0
  for c in p:
    if c == 'R':
      rev += 1
    else:
      if rev % 2 == 0:
        dq.popleft()
      else:
        dq.pop()
  if rev % 2 != 0:
    dq.reverse()
  print('[' + ','.join(dq)+']')
    