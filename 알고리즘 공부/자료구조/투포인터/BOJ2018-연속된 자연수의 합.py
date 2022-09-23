n = int(input())

count = 1
sum = 1
start = 1
end = 1

while end < n:
    if sum == n:
        count += 1
        end += 1
        sum += end
    elif sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
        
print(count)