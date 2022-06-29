# 문제 : 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
'''
팰린드롬이란,
앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장을 일컫는다.
'''

def solution(s):
    str1 = ''
    for i in s:
        if i.isalpha() or i.isdigit():
            str1 += i.lower()
    str2 = str1[::-1]
    return str1 == str2
    
# 테스트 케이스
print(solution("A man, a plan, a canal: Panama"))
print(solution(",,,,,,"))
print(solution("race a car"))

# 블로그 정리 : https://jyostudy.tistory.com/73
