function solution(n) {
    return (n**0.5) % 1 === 0 ? ((n**0.5) +1)**2 : -1;
}