import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
N = list(map(int, input().split()))

N.sort() # 투 포인터 쉽게 사용하기 위해 정렬

s = 0 # start_index
e = n-1 # end_index
sum = N[s] + N[e]
count = 0

while s < e:
    if sum < m:
        sum -= N[s]
        s += 1
        sum += N[s]
    elif sum > m:
        sum -= N[e]
        e -= 1
        sum += N[e]
    else:
        count += 1
        sum -= N[s]
        sum -= N[e]
        s += 1
        e -= 1
        sum += N[s]
        sum += N[e]


print(count)

# 블로그 정리 : https://jyostudy.tistory.com/92