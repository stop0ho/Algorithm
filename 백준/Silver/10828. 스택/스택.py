import sys
input = sys.stdin.readline
n = int(input())
stk = [] 
for _ in range(n):
    x = list(map(str,input().split()))
    if x[0] =='push':
        stk.append(int(x[1]))
    elif x[0] =='pop':
        if stk:
            print(stk.pop())
        else:
            print('-1')
    elif x[0] =='size':
        print(len(stk))
    elif x[0] =='empty':
        if stk:
            print('0')
        else:
            print('1')
    elif x[0] =='top':
        if stk:
            print(stk[-1])
        else:
            print('-1')