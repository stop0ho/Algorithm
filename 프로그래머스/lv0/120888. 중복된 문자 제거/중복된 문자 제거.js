function solution(my_string) {
    let answer = '';
    for (let i=0; i<my_string.length; i++){
        if (answer.includes(my_string[i]) === false) {
            answer += my_string[i]
        }
    }
    return answer;
}