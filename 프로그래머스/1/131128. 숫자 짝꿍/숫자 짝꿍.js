function solution(X, Y) {
    var answer = '';
    
    let mapX = new Map()
    let mapY = new Map()
    
    for (const num of X) {
        mapX.set(num, mapX.has(num) ? mapX.get(num) + 1 : 1)
    }
    for (const num of Y) {
        mapY.set(num, mapY.has(num) ? mapY.get(num) + 1 : 1)
    }
    
    for (const [k, v] of mapX) {
        if (mapY.get(k) == v) answer += k.repeat(v)
        else answer += k.repeat(Math.min(mapY.get(k), v))
    }
    
    if (answer.length === 0) return '-1'
    if (answer.length === answer.split('').filter((v) => v === '0').length) return '0'
    
    return answer.split('').sort((a, b) => b-a).join('')
    
}