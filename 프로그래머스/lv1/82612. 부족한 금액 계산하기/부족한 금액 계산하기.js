function solution(price, money, count) {
    let answer = 0;

    for (let i=1; i<count+1; i++) {
        answer += price * i
    }
    
    return money - answer < 0 ? answer - money : 0;
}