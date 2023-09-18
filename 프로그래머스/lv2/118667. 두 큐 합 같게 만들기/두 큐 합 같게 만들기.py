from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1 + sum2) // 2
    
    cnt = 0
    
    while True:
        if sum1 == target and sum2 == target:
            break
        if sum1 < target:
            p = q2.popleft()
            q1.append(p)
            sum2 -= p
            sum1 += p
            cnt += 1
        elif sum2 < target:
            p = q1.popleft()
            q2.append(p)
            sum1 -= p
            sum2 += p
            cnt += 1
        if cnt > len(queue1) * 4:
            return -1
    return cnt