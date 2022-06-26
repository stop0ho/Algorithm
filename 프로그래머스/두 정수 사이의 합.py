import time

def solution(a, b):
    sum = 0
    maxi = max(a, b)
    mini = min(a, b)
    for i in range(mini, maxi+1):
        sum += i
    return sum

# 테스트 케이스
start = time.time()
print(solution(3, 5))
print(solution(5, 3))

print("time : ", time.time() - start)

# 깨달은 점 : python에는 sum 함수가 있고, range 지정이 가능하다.
# 예)
print(sum(range(3, 6)))


# 따라서 다음과 같이 개선 가능
def better_solution(a, b):
    return sum(range(min(a, b), max(a,b)+1))

start = time.time()

print(better_solution(3, 5))
print(better_solution(5, 3))

print("time : ", time.time() - start)

# 수행 시간은 비슷비슷하다.