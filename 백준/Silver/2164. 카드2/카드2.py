from collections import deque

n = int(input())
C = deque(range(1, n+1))

while len(C) > 1:
    C.popleft()
    C.append(C.popleft())
    
print(C[0])