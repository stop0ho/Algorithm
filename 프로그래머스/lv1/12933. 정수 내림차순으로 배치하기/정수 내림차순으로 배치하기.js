function solution(n) {
    var answer = 0;
    n = n.toString();
    answer = n.split('').map(Number);
    answer.sort((a, b) => b-a);
    return Number(answer.join(''));
}