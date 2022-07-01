def solution(s):
    mapping = ['zero', 'one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine']
    
    answer = ''
    
    left_p = 0
    right_p = 0
    
    while left_p < len(s) and right_p < len(s):
        word = s[left_p : right_p + 1]
        if word.isdigit():
            answer += str(word)
            left_p += 1
            right_p = left_p       
        elif word in mapping:
            answer += str(mapping.index(word))
            left_p = right_p + 1
            right_p = left_p
        else:
            right_p += 1
            
    
    return int(answer)

# 테스트케이스
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))


# 딕셔너리를 이용한 간단한 풀이
def solution_2(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution_2("one4seveneight"))
print(solution_2("23four5six7"))
print(solution_2("2three45sixseven"))
print(solution_2("123"))

# 블로그 정리 : https://jyostudy.tistory.com/78?category=1105961
