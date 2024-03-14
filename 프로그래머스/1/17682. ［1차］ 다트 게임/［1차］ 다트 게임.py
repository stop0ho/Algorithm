def solution(dartResult):
    bonus = [" ", "S", "D", "T"]

    score = []
    square = []
    option = []
    
    i = 0
    while i < len(dartResult):
        try:
            if dartResult[i+1].isdigit():
                score.append(int(dartResult[i:i+2]))
                i += 2
            else:
                score.append(int(dartResult[i]))
                i += 1
        except:
            if dartResult[i] in bonus: square.append(bonus.index(dartResult[i]))
            i += 1
            
            if i < len(dartResult):
                if dartResult[i].isdigit():
                    option.append(' ')
                else:
                    option.append(dartResult[i])
                    i += 1
    if len(option) != 3:
        option.append(' ')
    
    
    for i in range(0, 3):
        score[i] = pow(score[i], int(square[i]))
        if option[i] == '*':
            try:
                if i-1 >= 0:
                    score[i-1] *= 2
                score[i] *= 2
            except:
                pass
        elif option[i] == '#':
            score[i] *= -1
        else:
            pass

    return sum(score)