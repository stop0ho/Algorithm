const divisorCnt = (n) => {
    let cnt = 0;
    for (let i=1; i<=n/2; i++){
        if (n % i === 0) cnt += 1
    }
    return cnt + 1
}

function solution(number, limit, power) {
    let answer = [];
    
    for (let i=1; i<number+1; i++){
        answer.push(divisorCnt(i))
    }
    
    answer = answer.map((v) => v <= limit ? v : power)
    
    return answer.reduce((a, c) => a+c);
}