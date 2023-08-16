N = input()

'''
def bin(n):
    ans = ''
    while n > 1:
        r = n % 2
        n //= 2
        ans += str(r)
    ans += str(n)
    if len(ans) < 3:
        ans += '0' * (3 - len(ans))
    return ans[::-1]


for c in N:
    ans += bin(int(c))

ans = ans.lstrip('0')
print(ans)
'''
ans = bin(int(N, 8))
ans = ans.replace('0b', '')
print(ans)
