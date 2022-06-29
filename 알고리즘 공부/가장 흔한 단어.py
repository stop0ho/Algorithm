'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며,
구두점(마침표, 쉼표) 또한 무시한다
'''
import re

def solution(paragraph, banned):
    # re.sub(pattern, repl, string, count=0 flags=0)
    # re.sub(패턴(정규식), 바꿀 문자열, '문자열', 바꿀 횟수)
    # count가 생략이면 찾은 문자열을 모두 치환

    # 정규식에서 ^는 not, \w는 단어 문자를 뜻함. 따라서 이 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.
    words = [word.lower() for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    # 딕셔너리 초기화
    counts = {word: 0 for word in words}

    for i in words:
        counts[i] += 1

    return max(counts, key=counts.get)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(solution(paragraph, banned))

# 블로그 정리 : https://jyostudy.tistory.com/75?category=1107038