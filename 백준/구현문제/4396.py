n = int(input())
cnt = [[0] * n for _ in range(n)]

for i in range(n):
    row = input()
    for j in range(n):
        if row[j] == '*':
            for index in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                if 0 <= i + index[0] <= n-1 and 0 <= j + index[1] <= n-1:
                    if cnt[i+index[0]][j+index[1]] != '*':
                        cnt[i+index[0]][j+index[1]] += 1
                cnt[i][j] = '*'

fail = False
user = [input() for _ in range(n)]
ans = ['' for _ in range(n)]
for i in range(n):
    for j in range(n):
        if user[i][j] == 'x':
            if cnt[i][j] == '*':
                fail = True
            else:
                ans[i] += str(cnt[i][j])
        else:
            ans[i] += '.'
    if fail: break

