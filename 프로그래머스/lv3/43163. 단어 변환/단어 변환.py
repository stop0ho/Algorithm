from collections import defaultdict
from collections import deque

def solution(begin, target, words):
    answer = -1
    if target not in words:
        return 0
    
    graph = defaultdict(list)
    
    words.append(begin)
    l = len(words[0])
    for word1 in words:
        for word2 in words:
            diff = 0
            for k in range(l):
                if word1[k] != word2[k]:
                    diff += 1
            if diff == 1:
                graph[word1].append(word2)

    visited = {word : False for word in words}
    q = deque([(begin, 0)])
    visited[begin] = True
    while q:
        v, step = q.popleft()
        if v == target:
            return step
        for word in graph[v]:
            if not visited[word]:
                q.append((word, step+1))
                visited[word] = True
    return 0