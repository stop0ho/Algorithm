def solution(numbers, hand):
    answer = ''
    
    keypad = [[1,2,3], [4,5,6], [7,8,9], ['*', 0, '#']]
    left = [3, 0]
    right = [3, 2]
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            i = [1, 4, 7].index(num)
            left = [i, keypad[i].index(num)]
        elif num in [3, 6, 9]:
            answer += 'R'
            i = [3, 6, 9].index(num)
            right = [i, keypad[i].index(num)]
        elif num in [2, 5, 8, 0]:
            i = [2, 5, 8, 0].index(num)
            cnt = [i, keypad[i].index(num)]
            sub_l = abs(left[0] - cnt[0]) + abs(left[1] - cnt[1])
            sub_r = abs(right[0] - cnt[0]) + abs(right[1] - cnt[1])
            if sub_l < sub_r:
                left = cnt
                answer += "L"
            elif sub_l > sub_r:
                right = cnt
                answer += "R"
            else:
                if hand == 'left':
                    left = cnt
                    answer += "L"
                else:
                    right = cnt
                    answer += "R"
        
    return answer

# 테스트 케이스
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))