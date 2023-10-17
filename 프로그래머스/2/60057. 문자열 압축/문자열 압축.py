def solution(s):
    answer = len(s) # 최대 길이
    # 1은 생략해야함
    for i in range(1, len(s)//2 + 1):
        result = ''
        
        word = s[0:i]
        start = 0
        end = i
        dup = 1
        while end <= len(s):
            start = end
            end += i
            temp = s[start:end]
            if word == temp:
                dup += 1
            else:
                if dup > 1:
                    result += (str(dup) + word)
                else:
                    result += word
                word = temp
                dup = 1
        result += s[i * (len(s) // i):]
        if len(result) < answer:
            answer = len(result)
        
    return answer