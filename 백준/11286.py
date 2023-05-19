from queue import PriorityQueue
import sys

input = sys.stdin.readline

N = int(input())
q = PriorityQueue()

for _ in range(N):
    num = int(input())
    if num == 0: # 0이 입력되면 우선순위 큐가 비었는지 먼저 판단
        if q.empty(): # 만약 비었다면
            print(0) # 0 출력
        else: # 아니면
            print(q.get()[1]) # 가장 작은 값 출력
    else:
        q.put((abs(num), num)) # 절댓값을 우선순위로 해서 수 삽입
