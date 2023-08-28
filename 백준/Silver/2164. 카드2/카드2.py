from collections import deque

n = int(input())
list = []
for i in range(1,n+1):
    list.append(i)
list = deque(list)

while len(list) > 0:
    if len(list) == 1:
        print(list[0])
        break
    list.popleft()
    list.append(list[0])
    list.popleft()