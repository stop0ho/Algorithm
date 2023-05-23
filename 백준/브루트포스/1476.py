E, S, M = map(int, input().split())
e = 1
s = 1
m = 1

year = 1
while True:
    if E == e and S == s and M == m:
        print(year)
        break

    e += 1
    s += 1
    m += 1

    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

    year += 1