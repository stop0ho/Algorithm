function solution(s, skip, index) {
    var answer = '';
    let alpha = '';
    for (let i=97; i <= 122; i++) {
        let a = String.fromCharCode(i);
        if (skip.includes(a)) continue
        alpha += a
    }
    let l = alpha.length;
    for (const c of s) {
        answer += (alpha[(alpha.indexOf(c) + index) % l])
    }
    return answer;
}