from collections import deque

def solution(msg):
    answer = []
    d = {chr(x):x-64 for x in range(65, 91)}
    next_index = 27
    
    while True:
        if msg in d:
            answer.append(d[msg])
            break
            
        w = msg[0]
        for i in range(1, len(msg)):
            if w + msg[i] not in d:
                c = msg[i]
                answer.append(d[w])
                d[w+c] = next_index
                next_index += 1
                msg = msg[i:]
                break
            else:
                w += msg[i]
     
        
    return answer