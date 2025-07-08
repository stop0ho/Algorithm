function solution(s) {
    let midIndex = Math.floor(s.length / 2);
    return s.length % 2 === 0 ? s[midIndex - 1] + s[midIndex] : s[midIndex];
}