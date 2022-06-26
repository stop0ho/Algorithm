def solution(s, n):
    lower = [chr(i) for i in range(ord("a"), ord("z")+1)]
    upper = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    
    result = ''
    
    for i in s:
        if i == ' ':
            result += ' '
        elif i.isupper():
            result += upper[(upper.index(i) + n) % 26]
        else:
            result += lower[(lower.index(i) + n) % 26]
    
    return result

# 테스트 케이스
print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))