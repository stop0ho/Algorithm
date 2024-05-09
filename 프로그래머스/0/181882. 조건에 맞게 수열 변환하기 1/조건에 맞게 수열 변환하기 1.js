function solution(arr) {
    let answer = []
    for (let num of arr) {
        if (num >= 50 && num % 2 === 0){
            answer.push(num/2)
            continue
        }
        if (num < 50 && num % 2 !== 0) {
            answer.push(num*2)
            continue
        }
        answer.push(num)
    }
    return answer;
}