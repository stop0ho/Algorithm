def solution(array):
    M = -1
    s = set(array)
    cnt = []
    for num in s:
        num_count = array.count(num)
        cnt.append([num, num_count])
        if M < num_count:
            M = num_count
    
    cnt.sort(key=lambda x: -x[1])
    if len(s) > 1:
        if cnt[0][1] == cnt[1][1]:
            return -1
        else:
            return cnt[0][0]
    else:
        return cnt[0][0]