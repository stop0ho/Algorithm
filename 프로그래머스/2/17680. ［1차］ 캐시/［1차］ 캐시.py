from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    # 대소문자 구분하지 않으므로 모두 소문자로 통일
    cities = [city.lower() for city in cities]
    
    q = deque([])
    l = 0

    for i in range(len(cities)):
        if l < cacheSize:
            if q and cities[i] in q:
                q.remove(cities[i])
                q.append(cities[i])
                answer += 1
            else:
                q.append(cities[i])
                answer += 5
                l += 1
        else:
            if q and cities[i] in q:
                q.remove(cities[i])
                q.append(cities[i])
                answer += 1
            else:
                if q:
                    q.popleft()
                q.append(cities[i])
                answer += 5

    return answer                
        