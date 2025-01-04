from collections import deque

def solution(queue1, queue2):
    # 두 큐를 deque로 변환
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 전체 합 계산
    total_sum = sum(queue1) + sum(queue2)
    
    # 전체 합이 홀수라면 불가능
    if total_sum % 2 != 0:
        return -1
    
    # 목표 합
    target = total_sum // 2
    
    # 두 큐를 이어붙인 형태
    combined_queue = queue1 + queue2
    n = len(queue1)
    
    # 투 포인터
    left, right = 0, n
    current_sum = sum(queue1)
    max_operations = 2 * len(combined_queue)  # 최대 이동 가능 횟수
    
    operations = 0
    while left < len(combined_queue) and right < len(combined_queue):
        if current_sum == target:
            return operations
        
        # 목표보다 작으면 오른쪽 포인터 이동 (값 추가)
        if current_sum < target:
            current_sum += combined_queue[right]
            right += 1
        # 목표보다 크면 왼쪽 포인터 이동 (값 제거)
        else:
            current_sum -= combined_queue[left]
            left += 1
        
        # 작업 횟수 증가
        operations += 1
        
        # 최대 이동 가능 횟수를 초과하면 불가능
        if operations > max_operations:
            return -1
    
    # 모든 경우에 대해 목표 달성이 불가능한 경우
    return -1
