def solution(num):
    answer = 0
    tmp_num = num
    while tmp_num != 1:
        if answer > 500:
            return -1
        if tmp_num % 2 == 0:
            tmp_num /= 2
        else:
            tmp_num = tmp_num * 3 + 1
        answer+=1
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))