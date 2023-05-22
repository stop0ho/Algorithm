from heapq import heappush, heappop

K, N = map(int, input().split())
nums = list(map(int, input().split()))
result = []

for i in range(0, len(nums)):
    heappush(result, nums[i])
    heappush(result, nums[i]**2)
    for j in range(i+1, len(nums)):
        heappush(result, nums[i]*nums[j])

print(result)