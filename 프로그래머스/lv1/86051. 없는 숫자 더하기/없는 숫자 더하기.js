function solution(numbers) {
    var answer = 45;
    for (let i in numbers) {
        answer -= numbers[i]
    }
    return answer;
}