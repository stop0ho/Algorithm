function solution(n) {
    n = n.toString();
    let answer = [...n];
    answer = answer.map(Number);
    return answer.reverse();
}