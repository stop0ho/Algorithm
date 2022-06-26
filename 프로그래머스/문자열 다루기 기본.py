# 내 코드
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if ord("0") > ord(s[i]) or ord(s[i]) > ord("9"):
                return False
        return True
    return False

'''
다른 솔루션도 가능하다
1. isdigit() 이용 : 문자열이 숫자인지 아닌지를 판별해주는 함수
2. try/except 사용
try/except는 다음과 같이 구성 된다.
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
'''

def solution_try_except(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6