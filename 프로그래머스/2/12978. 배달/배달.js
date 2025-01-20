function solution(N, road, K) {
    const graph = Array.from({length: N+1}, () => []);
    const distance = Array(N+1).fill(Infinity);
    distance[1] = 0;
    
    for (const [a, b, c] of road) {
        graph[a].push([b, c]);
        graph[b].push([a, c]);
    }
    
    const q = [[1, 0]]; // 현재 점, 거리
    while (q.length > 0) {
        q.sort((a, b) => a[1] - b[1]);
        const [i, d] = q.shift();
        
        if (d > distance[i]) continue;
        
        for (const [next, cost] of graph[i]) {
            const newD = d + cost;
            if (newD < distance[next]) {
                distance[next] = newD;
                q.push([next, newD]);
            }
        }
    }
    
    return distance.filter(d => d <= K).length;
    
}