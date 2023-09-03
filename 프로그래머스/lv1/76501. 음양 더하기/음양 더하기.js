function solution(absolutes, signs) {
    var answer = 0;
    for (const index in absolutes) {
        if (signs[index] === true) {
            answer += absolutes[index];
        } else {
            answer -= absolutes[index]
        }
    }
    return answer;
}