const isPrime = (n) => {
    if (n <= 1) return false;
    if (n % 2 === 0) return n === 2 ? true : false;
    const sqrt = parseInt(Math.sqrt(n))
    for (let div = 3; div <= sqrt; div += 2) {
        if (n % div === 0) return false
    }
    return true
}

const solution = (n) => {
    let answer = 0;
    
    for (let i=2; i<=n; i++){
        if (isPrime(i)) answer++
    }
    
    return answer
}