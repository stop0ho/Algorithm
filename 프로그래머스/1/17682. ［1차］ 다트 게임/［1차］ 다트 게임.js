function solution(dartResult) {
    let answer = [];
    
    let score = ''
    let bonus = ''
    let option = ''
    for (c of dartResult){
        if (Number(c) == c){
            score += c
            continue
        }
        if (c === 'S') {
            answer.push(Number(score))
        } else if (c === 'D') {
            answer.push(Number(score) ** 2)
        } else if (c === 'T') {
            answer.push(Number(score) ** 3)
        }
        score = ''
        
        if (c === '#') {
            answer.push(answer.pop() * -1)
        } else if (c === '*') {
            let num1 = answer.pop()
            if (answer.length > 0){
                let num2 = answer.pop()
                answer.push(num2 * 2)
            }
            answer.push(num1 * 2)
        }
        
    }
    return answer.reduce((a, c) => a+c);
}