def good(n1, n2, op):
    if op == '>':
        if n1 < n2:
            return False
    elif op == '<':
        if n1 > n2:
            return False
    return True

def go(index, num):
    if index == k+1:
        ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(num[index-1], str(i), s[index-1]):
            check[i] = True
            go(index+1, num+str(i))
            check[i] = False

k = int(input())
s = input().split()
ans = []
check = [False] * 10
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])