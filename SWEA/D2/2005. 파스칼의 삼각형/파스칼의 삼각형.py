T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    result = [[0] * i for i in range(1, n+1)]
    result[0][0] = 1
    for i in range(1, n):
        for j in range(0, i+1):
            cur = 0
            if j-1 >= 0:
                cur += result[i-1][j-1]
            if j < i:
                cur += result[i-1][j]
            result[i][j] = cur
    print('#%d' % (test_case))
    for l in result:
        print(*l)