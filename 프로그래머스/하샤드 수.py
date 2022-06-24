def solution(x):
    sum = 0
    tmp = x
    for i in range(len(str(x))-1, -1, -1):
        sum += tmp // pow(10, i)
        tmp = tmp % pow(10, i)
    
    return x % sum == 0