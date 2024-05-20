function solution(s) {
    var answer = 0;
    let first = ''
    let fc = 0
    let ac = 0
    for (const c of s) {
        if (first === '') first = c;
        
        if (c === first) fc += 1
        else ac += 1
        
        if (ac === fc) {
            answer += 1
            fc = 0
            ac = 0
            first = ''
        }
    }
    return ac !== fc ? answer + 1: answer;
}