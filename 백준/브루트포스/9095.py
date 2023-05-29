'''
count : 사용한 수의 개수
sum : 합
'''
def go(count, sum, n):
    if sum == n:
        global result
        result += 1
        return
    if sum > n:
        return
    for i in range(1, 4):
        go(count+1, sum+i, n)
        
t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    go(0, 0, n)
    print(result)