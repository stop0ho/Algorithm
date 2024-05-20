function solution(lottos, win_nums) {
    let rank = [6, 6, 5, 4, 3, 2, 1]
    let zeroCnt = 0;
    let correct = 0;
    
    for (const num of lottos) {
        if (win_nums.includes(num)) correct += 1
        if (num === 0) zeroCnt += 1
    }
    
    return [rank[correct+zeroCnt], rank[correct]];
}