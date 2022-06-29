'''
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 숫자에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다. 
'''

'''
[ ] 코너 케이스 : '문자가 동일한 경우' - 식별자 순으로
[ ] 숫자 로그는 입력 순서대로 -> 문자, 숫자를 따로
'''


def solution(logs: list[str]):
    digit = []
    letters = []

    for log in logs:
        if log.split()[1].isdigit():
            digit.append(log)
        else:
            letters.append(log)
    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digit

# test case
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(solution(logs))


# 블로그 포스트 : https://jyostudy.tistory.com/74