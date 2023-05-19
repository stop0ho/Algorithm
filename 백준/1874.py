''' 
attend = push
pop = pop (맨 마지막 원소 제거)
'''

n = int(input())

stack = []
p = True
num = 0
result = []



for _ in range(n):
    m = int(input())
    if num <= m:
        while num < m:
            num += 1
            stack.append(num)
            result.append('+')
        stack.pop()
        result.append('-')
    else:
        if stack[-1] == m:
            stack.pop()
            result.append('-')
        else:
            p = False

if p:
    for i in result:
        print(i)
else:
    print("NO")