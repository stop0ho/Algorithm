def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer

# 테스트 케이스
print(solution(3))
print(solution(4))
