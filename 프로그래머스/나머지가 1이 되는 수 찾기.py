def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i
        
        
# 테스트 케이스
print(solution(10))
print(solution(12))