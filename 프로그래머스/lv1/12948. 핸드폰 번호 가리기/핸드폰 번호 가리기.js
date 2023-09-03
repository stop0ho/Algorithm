function solution(phone_number) {
    var answer = '*'.repeat(phone_number.length - 4)
    answer += phone_number.slice(-4)
    return answer;
}