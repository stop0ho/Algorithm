def solution(arr, divisor):
    arr.sort()
    result = [i for i in arr if i % divisor == 0]
    return result if len(result) != 0 else [-1]

# 테스트 케이스
print(solution([5, 9, 7, 10], 5))
print(solution([3, 2, 6], 10))