from itertools import combinations
from collections import deque

def solution(relation):
    answer = 0
    
    lr = len(relation)
    lc = len(relation[0])
    col_list = []
    for i in range(lc):
        col_list.append(list(zip(*relation))[i])
    
    comb = []
    for i in range(1, lc+1):
        comb.extend(combinations(range(lc), i))    
    
    unique = []
    for i in comb:
        new_col = set(zip(*[col_list[c] for c in i]))
        # 유일성 검증
        if len(new_col) == lr:
            # 최소성 검증
            for x in unique:
                if set(x).issubset(set(i)):
                    break
            else:
                unique.append(i)
    
    return len(unique)