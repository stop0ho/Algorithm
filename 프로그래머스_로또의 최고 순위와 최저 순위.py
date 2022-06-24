def solution(lottos, win_nums):
    '''
    🤩순위를 딕셔너리로 표현
    key : 맞은 개수
    value : 순위
    '''
    rank = {6: 1, 5: 2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    min = 0
    for i in lottos:
        if i in win_nums:
            min += 1
    
    max = min + lottos.count(0)

    answer = [rank[max], rank[min]]
    return answer


print(solution([0,0,1,25,31,44],[1,6,10,19,31,45]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))