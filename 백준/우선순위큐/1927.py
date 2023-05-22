from queue import PriorityQueue
import sys

input = sys.stdin.readline

q = PriorityQueue()
N = int(input())

for _ in range(N):
    num = int(input())
    if num == 0:
        if q.empty():
            print(0)
        else:
            print(q.get()[1])
    else:
        q.put((num, num))
