function solution(numbers) {
    let answer = Array(10).fill(0).map((_, i) => i).reduce((acc, cur) => acc + cur);
    
    for (const num of numbers) {
        answer -= num;
    }
    
    return answer;
}