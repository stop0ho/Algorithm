def solution(record):
    answer = []
    
    d = {}
    for s in record:
        s = s.split()
        if s[0] == 'Enter' or s[0] == 'Change':
            d[s[1]] = s[2]
    
    for s in record:
        s = s.split()
        if s[0] == "Enter":
            answer.append('%s님이 들어왔습니다.' % d[s[1]])
        elif s[0] == "Leave":
            answer.append('%s님이 나갔습니다.' % d[s[1]])
    return answer