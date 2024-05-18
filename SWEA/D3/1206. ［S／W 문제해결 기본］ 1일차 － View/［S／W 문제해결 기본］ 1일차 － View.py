for test_case in range(1, 11):
    N = int(input())
    L = list(map(int, input().split()))
    sum = 0
    for i in range(2, N-2):
        left = max(L[i-1], L[i-2])
        right = max(L[i+1], L[i+2])
        if L[i] > left and L[i] > right:
            sum += L[i] - max(left, right)
    print('#%d %d'%(test_case, sum))
            
