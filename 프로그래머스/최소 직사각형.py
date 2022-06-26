'''
아이디어 : 가로가 세로보다 짧으면 둘을 바꾸면 된다.
'''

def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    w = [i[0] for i in sizes]
    h = [i[1] for i in sizes]
    return max(w) * max(h)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# 다른 방법 : swap말고 그냥 정렬 하고 시작하는 방법도 있음. 그러면 max 안 쓰고 그냥 인덱스로 접근할 수 있게 됨.