import collections

def solution(tickets):
    answer = []
    graph = collections.defaultdict(list)
    
    def dfs(s):
        while graph[s]:
            dfs(graph[s].pop(0))
        
        if not graph[s]:
            answer.append(s)
            return
            
    
    for a, b in tickets:
        graph[a].append(b)
    for a, b in graph.items():
        graph[a].sort()
    
    dfs('ICN')
    return answer[::-1]