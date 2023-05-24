from itertools import combinations

n, m, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

max = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        temp = p[i][j]
        # 일차원 리스트로 만들기
        nums = sum(p, [])
        
        nums.remove(p[i][j])
        # 세로에서 지우기
        if n > 1:
            if i == 0:
                nums.remove(p[i+1][j])
            elif i == n-1:
                nums.remove(p[i-1][j])
            else:
                nums.remove(p[i+1][j])
                nums.remove(p[i-1][j])

        if m > 1:
            # 가로에서 지우기
            if j == 0:
                nums.remove(p[i][j+1])
            elif j == m - 1:
                nums.remove(p[i][j-1])
            else:
                nums.remove(p[i][j-1])
                nums.remove(p[i][j+1])

        com = combinations(nums, k-1)
        for c in com:
            if len(c) > 1:
                m = max(c)
            elif len(c) == 1:
                m = c[0]
            else:
                m = 0
            if temp + m > max:
                max = temp + m
        

print(max)