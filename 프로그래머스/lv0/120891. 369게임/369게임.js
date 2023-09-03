function solution(order) {
    let answer = 0
    order = order.toString();
    for (var i=0; i<order.length; i++) {
        if (order[i] == '3' || order[i] == '6' || order[i] == '9') {
            answer += 1
        }
    }
    return answer;
}