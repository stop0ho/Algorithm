function solution(k, score) {
    var answer = [];
    
    let mj = [];
    for (let i=0; i<score.length; i++){
        if (i<k) mj.push(score[i])
        else{
            if (mj[k-1] < score[i]){
                mj.pop()
                mj.push(score[i])
            }
        }
        mj.sort((a, b) => b-a)
        answer.push(mj.at(-1))
    }
    
    return answer;
}