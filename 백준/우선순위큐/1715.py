from queue import PriorityQueue

q = PriorityQueue()
N = int(input())
sum = 0

for _ in range(N):
  num = int(input())
  q.put((num, num))

while q.qsize() >= 2:
  a = q.get()[1]
  b = q.get()[1]
  newN = a + b
  q.put((newN, newN))
  sum += newN

print(sum)