function solution(k, m, score) {
    var answer = 0;
    score.sort((a, b) => b-a)
    let apple = score.slice(0, m * Math.floor(score.length / m))
    for (let i=m-1; i<apple.length; i+=m) {
        answer += (m * apple[i])
    }
    return answer;
}