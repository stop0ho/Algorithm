const diff = (str1, str2) => {
    let d = 0;
    for (let i=0; i<str1.length; i++) {
        if (str1[i] !== str2[i]) d++;
    }
    return d;
}

function solution(begin, target, words) {
    let q = [[begin, 0]]
    let visited = new Array(words.length).fill(false)
    
    while (q.length !== 0) {
        let [s, d] = q.shift()
        if (s === target) return d
        for (const i in words) {
            if (!visited[i] && diff(words[i], s) === 1) {
                visited[i] = true // 방문처리
                q.push([words[i], d+1])
            }
        }
        
    }
    
    return 0;
}