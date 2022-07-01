def solution(board, moves):
    answer = 0
    
    # 이차원 리스트를 stack처럼 구현
    stack = [[] for _ in range(len(board))]
    for i in board:
        for index, j in enumerate(i):
            if j != 0:
                stack[index].append(j)
    
    # 결과 스택
    result_stack = []
    
    for i in moves:
        if len(stack[i-1]) != 0:
            if len(result_stack) != 0 and result_stack[len(result_stack) - 1] == stack[i-1][0]:
                result_stack.pop()
                answer += 2
            else:
                result_stack.append(stack[i-1][0])
            del stack[i-1][0]

    return answer

# 테스트 케이스
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

'''
새로 알게된 것:
이차원 리스트 초기화 코드 : stack = [[] for _ in range(len(board))]
블로그 정리 : https://jyostudy.tistory.com/79?category=1105961
'''