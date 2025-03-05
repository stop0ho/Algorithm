function solution(players, m, k) {
    // 서버가 현재 시점에서 몇대가 증설되어있어야 하는지
    // k만큼의 시간동안 -> 어떻게 관리해야할지
    let answer = 0;
    
    let servers = Array.from({length: players.length}, () => 0);
    
    for (let i=0; i<players.length; i++) {
        const required = Math.floor(players[i] / m)
        if (required > 0 && servers[i] < required) {
            const plus = required - servers[i]
            answer += plus;
            for (let j=0; j<k; j++) {
                servers[i+j] += plus;
            }
        }
    }
    
    console.log(servers)
    
    return answer;
}