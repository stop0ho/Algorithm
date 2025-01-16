function solution(n, lost, reserve) {
    // 여벌 체육복을 가져온 학생이 도난당한 경우 다른 학생에게 체육복을 빌려줄 수 없다.
    let filtered_lost = lost.filter((v) => !reserve.includes(v));
    let filtered_reserve = reserve.filter((v) => !lost.includes(v));
    
    // 정렬
    filtered_lost.sort((a, b) => a - b);
    filtered_reserve.sort((a, b) => a - b);
        
    // 체육복 빌려줌
    for (let i=0; i<filtered_reserve.length; i++) {
        let index = filtered_lost.findIndex((student) => Math.abs(filtered_reserve[i] - student) === 1);
        if (index !== -1) filtered_lost.splice(index, 1);
    }
    
    return n - filtered_lost.length;
}