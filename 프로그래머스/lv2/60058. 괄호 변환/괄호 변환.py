from collections import deque

def is_valid(s):
    stack = deque([])
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def split_uv(s):
    cnt1 = 0
    cnt2 = 0
    u = ''
    for c in s:
        u += c
        if c == '(':
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 == cnt2:
            break
    v = s.replace(u, '', 1)
    return [u, v]

def solution(p):
    if not p:
        return ''
    if is_valid(p):
        return p
    else:
        u, v = split_uv(p)
        if is_valid(u):
            return u + solution(v)
        else:
            answer = '('
            answer += solution(v)
            answer += ')'
            u = list(u)[1:len(u)-1]
            u = ''.join(u)
            for c in u:
                if c == ')':
                    answer += '('
                else:
                    answer += ')'
            return answer
        
    
        
            