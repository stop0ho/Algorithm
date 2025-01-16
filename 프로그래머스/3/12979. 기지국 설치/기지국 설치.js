function solution(n, stations, w) {
    let answer = 0;
    
    let i = 1;
    let station_index = 0; // 이미 설치된 기지국 탐색 용도
    
    while (i <= n) {
        if (station_index < stations.length && i >= stations[station_index] - w) {
            i = stations[station_index] + w + 1;
            station_index++;
        } else {
            answer++;
            i += w * 2 + 1;
        }
    }
    
    return answer
}