function solution(n, m, section) {
    var answer = 0;
    
    if (m === 1) return section.length;
    
    while (section.length > 0) {
        let start = section.shift()
        answer++
        for (let i=1; i<m; i++) {
            if (start + i === section[0]) section.shift()
        }
    }
    return answer;
}