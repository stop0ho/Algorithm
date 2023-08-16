def bingo(p, check, n):
    bing = 0

    r_cnt = 0
    c_cnt = 0
    b_cnt = 0
    b_cnt_r = 0
    # 줄 체크
    for i in range(5):
        if check[p[n][0]][i] == True:
            r_cnt += 1
    if r_cnt == 5:
        bing += 1
    # 열 체크
    for i in range(5):
        if check[i][p[n][1]] == True:
            c_cnt += 1
    if c_cnt == 5:
        bing += 1
    # 대각선 체크
    if p[n] in [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]:
        for i in range(5):
            if check[i][i] == True:
                b_cnt += 1
    if b_cnt == 5:
        bing += 1
    if p[n] in [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]:
        for i in range(5):
            if check[i][4-i] == True:
                b_cnt_r += 1
    if b_cnt_r == 5:
        bing += 1

    return bing


cnt = 0
bing = 0
res = 0

p = {i: [] for i in range(1, 26)}
check = [[False]*5 for _ in range(5)]
flag = False
for i in range(5):
    pan = list(map(int, input().split()))
    for j in range(5):
        p[pan[j]].append(i)
        p[pan[j]].append(j)


for i in range(5):
    call = list(map(int, input().split()))
    for c in call:
        cnt += 1
        check[p[c][0]][p[c][1]] = True
        bing += bingo(p, check, c)
        if bing >= 3:
            res = cnt
            flag = True
            break
    if flag:
        break

print(res)
