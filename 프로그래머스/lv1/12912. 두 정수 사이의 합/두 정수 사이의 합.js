function solution(a, b) {
    let answer = 0;
    let M, m;
    if (a > b) {
        M = a;
        m = b;
    } else {
        M = b;
        m = a;
    }
    for (let i=m; i<=M; i++){
        answer += i;
    }
    return answer;
}