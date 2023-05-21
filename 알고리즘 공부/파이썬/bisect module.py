import bisect

nums = [0, 1, 2, 3, 4, 5]
print(bisect.bisect_left(nums, 3)) # 3
print(bisect.bisect_right(nums, 3)) # 4


nums = [0, 1, 2, 3, 4, 5]
bisect.insort_left(nums, 3)
print(nums) # [0, 1, 2, 3, 3, 4, 5]

nums = [0, 1, 2, 3, 4, 5]
bisect.insort_right(nums, 3)
print(nums) # [0, 1, 2, 3, 3, 4, 5]

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    i = bisect.bisect([60, 70, 80, 90], score) # 점수를 삽입할 위치
    grades = 'FDCBA'
    print(grades[i], end = ' ') # F A C C B A A