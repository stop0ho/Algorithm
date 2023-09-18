def solution(numbers, target):
    def go(idx, sum):
        nonlocal answer
        if idx == len(numbers):
            if sum == target:
                answer += 1
            return 
            
        go(idx+1, sum+numbers[idx])
        go(idx+1, sum-numbers[idx])
    
    answer = 0
    go(0, 0)
    return answer

