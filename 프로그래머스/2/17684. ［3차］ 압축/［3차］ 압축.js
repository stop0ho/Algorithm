function solution(msg) {
    var answer = [];
    
    // 1. 딕셔너리 초기화
    const dict = new Map();
    for (let i=0; i<26; i++) {
        dict.set(String.fromCharCode(65 + i), i+1);
    }
    
    // 2. 현재 입력과 일치하는 가장 긴 문자열 찾기
    let msgArray = msg.split('')
    let cur = ''
    while (msgArray.length > 0) {
        cur += msgArray.shift()
        if (dict.get(cur)) continue
        answer.push(dict.get(cur.slice(0, -1)))
        dict.set(cur, dict.size + 1)
        msgArray.unshift(cur.slice(-1))
        cur = ''
    }
    
    if (cur !== '') {
    answer.push(dict.get(cur));
    }
    
    return answer;
}