def go(index, first, second):
    if index == n:
        if len(first) < 1:
            return -1
        if len(second) < 1:
            return -1
        t1 = 0
        t2 = 0
        for i in range(len(first)):
            for j in range(len(first)):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]

        for i in range(len(second)):
            for j in range(len(second)):
                if i == j:
                    continue
                t2 += s[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff
    
    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != - 1 and ans > t1):
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))