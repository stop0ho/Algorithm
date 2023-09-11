def solution(X, Y):
    answer = ''
    x = [0] * 10
    y = [0] * 10
    for num in X: x[int(num)] += 1
    for num in Y: y[int(num)] += 1
    for i, cnt in enumerate(x):
        if cnt != 0 and y[i] != 0:
            answer += str(i) * min(cnt, y[i])
    answer = sorted(list(answer), reverse = True)
    if not answer: return '-1'
    if answer[0] == '0': return '0'
    return ''.join(answer)