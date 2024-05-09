function solution(arr) {
    return arr.map((num) => {
        if (num >= 50 && num % 2 === 0) return num / 2
        if (num < 50 && num % 2 !== 0 ) return num * 2
        return num
    })
}