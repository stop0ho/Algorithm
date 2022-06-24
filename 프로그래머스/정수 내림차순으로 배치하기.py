def solution(n: int):
    str_list = list(str(n))
    str_list.sort()
    str_list.reverse()
    str_n = ""
    for i in str_list:
        str_n += i
    
    return int(str_n)

print(solution(118372))
print(solution(324523))
