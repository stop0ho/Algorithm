N = int(input())
answer = []
for i in range(1, N+1):
    si = str(i)
    cur = ''
    if '3' in si or '6' in si or '9' in si:
        cur += si.count('3') * '-'
        cur += si.count('6') * '-'
        cur += si.count('9') * '-'
        answer.append(cur)
    else:
        answer.append(si)
        
print(' '.join(answer))
        