def notation(n, q):
    m = ['A', 'B', 'C', 'D', 'E', 'F']
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base += m[mod%10]
        else: rev_base += str(mod)
    return rev_base[::-1]

def solution(n, t, m, p):
    answer = ''
    number = 1
    result = '0'
    
    for _ in range(t * m):
        result += notation(number, n)
        number += 1
    p -= 1
    for _ in range(t):
        answer += result[p]
        p += m
    return answer