function solution(dartResult) {
    let answer = [];
    const bonusScore = {
        'S': 1,
        'D': 2,
        'T': 3,
    }
    const options = {
        '*': 2,
        '#': -1,
        undefined: 1,
    }
    const reg = /[\d]+[SDT][*#]*/g;
    const darts = dartResult.match(reg);
    
    for (let i=0; i<darts.length; i++) {
        let [_, score, bonus, option ] = darts[i].match(/(^\d{1,})(S|D|T)(\*|#)?/)
        
        if (option === '*' && answer.length !== 0) answer[answer.length-1] *= options['*']
        
        answer.push(Math.pow(score, bonusScore[bonus]) * options[option])
    }
    return answer.reduce((a, c) => a+c);
}