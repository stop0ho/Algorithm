function solution(babbling) {
    var answer = 0;
    let able = ['aya', 'ye', 'woo', 'ma']
    
    // 연속해서 같은 발음 할 수 없음
    for (b of babbling) {
        let tmp = '';
        let l = [];
        let flag = false;
        for (c of b) {
            tmp += c
            if (able.includes(tmp)){
                if (l[l.length-1] === tmp){
                    flag = true
                    break
                }
                l.push(tmp)
                tmp = ''
            }
        }
        if (tmp == '' && !flag){
            answer += 1;
        }        
    }
    return answer;
}