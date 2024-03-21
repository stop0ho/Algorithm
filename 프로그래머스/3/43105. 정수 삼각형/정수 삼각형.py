def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    
    # 맨 윗 숫자 넣어주기
    dp[0][0] = triangle[0][0]
    for i in range(0, len(triangle) - 1):
        for j in range(0, i+1):
            # 왼쪽
            if dp[i+1][j] < dp[i][j] + triangle[i+1][j]:
                dp[i+1][j] = dp[i][j] + triangle[i+1][j]
            # 오른쪽
            if dp[i+1][j+1] < dp[i][j] + triangle[i+1][j+1]:
                dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]
    
    return max(dp[-1])