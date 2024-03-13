from collections import Counter

def make_set(s):
    result = []
    for i in range(0, len(s)-1):
        temp = ''
        if s[i].isalpha() and s[i+1].isalpha():
            result.append((s[i]+s[i+1]).upper())
    return result

def solution(str1, str2):
    answer = 0
    
    str1 = make_set(str1)
    str2 = make_set(str2)
    
    count1 = Counter(str1)
    count2 = Counter(str2)
    
    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
    if len(count1) == 0 and len(count2) == 0:
        return 65536
    
    inter = sum((count1 & count2).values())
    union = sum((count1 | count2).values())
        
    return int((inter / union) * 65536)