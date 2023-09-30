from collections import defaultdict
import math

def solution(fees, records):
    d = defaultdict(list)
    result = defaultdict(int)
    order = []
    # 정보 가공
    for record in records:
        time, number, io = record.split()
        if number not in d:
            order.append(number)
        d[number].append((time, io))
    
    # 마지막이 IN으로 끝나면 OUT을 추가해줌
    for number in d:
        if d[number][-1][1] == 'IN':
            d[number].append(('23:59', 'OUT'))
    
    # 시간계산 해서 result에 저장
    for number in d:
        target = d[number]
        for i in range(0, len(target), 2):
            out_time = int(target[i+1][0][0:2]) * 60 + int(target[i+1][0][3:])
            in_time = int(target[i][0][0:2]) * 60 + int(target[i][0][3:])
            result[number] += (out_time - in_time)
    
    # 요금 계산
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    answer = []
    order.sort()
    for number in order:
        time = result[number]
        if time <= default_time:
            answer.append(default_fee)
            continue
        answer.append(default_fee + math.ceil((time - default_time) / unit_time) * unit_fee)
            
    
    return answer