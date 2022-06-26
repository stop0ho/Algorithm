def solution(price, money, count):
    for i in range(1, count+1):
        money -= price * i
    return abs(money) if money < 0 else 0

# 테스트 케이스
print(solution(3, 20, 4))
print(solution(4, 12, 2))
print(solution(1, 12, 3))