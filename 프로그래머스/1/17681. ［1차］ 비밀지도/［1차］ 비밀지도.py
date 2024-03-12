def binary(n, l):
    # 우리가 아는 개념으로 2진수 구하는 코드
    result = ''
    while n > 0:
        n, mod = divmod(n, 2)
        result += str(mod)
    result = result[::-1]
    # 한 변의 길이보다 이진수의 길이가 짧으면 앞에 0 붙도록
    if len(result) < l:
        result = '0' * (l - len(result)) + result
    return result

def solution(n, arr1, arr2):
    result = ['' for _ in range(n)]
    
    bin_arr1 = [binary(i, n) for i in arr1]
    bin_arr2 = [binary(i, n) for i in arr2]
    
    for i in range(n):
        for j in range(n):
            if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
                result[i] += '#'
            else:
                result[i] += ' '
    
    return result