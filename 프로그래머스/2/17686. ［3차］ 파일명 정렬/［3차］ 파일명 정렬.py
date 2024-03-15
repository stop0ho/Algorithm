def solution(files):
    l = []
    
    for index, file in enumerate(files):
        head = ''
        number = ''
        isNumber = False
        
        for i in range(len(file)):
            if not file[i].isdigit():
                if not isNumber:
                    head += file[i].upper()
                else:
                    break
            else:
                isNumber = True
                number += file[i]
        
        number = int(number)
        l.append([head, number, file])
        
    l.sort(key=lambda x : (x[0], x[1]))
    answer = [i[2] for i in l]
        
    return answer
