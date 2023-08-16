N, K = map(int, input().split())
ans = 0

K = str(K)

for hour in range(0, N+1):
    if hour < 10:
        hour = '0' + str(hour)
    for minutes in range(0, 60):
        if minutes < 10:
            minutes = '0' + str(minutes)
        for seconds in range(0, 60):
            if seconds < 10:
                seconds = '0' + str(seconds)
            if K in str(hour) + str(minutes) + str(seconds):
                ans += 1

print(ans)