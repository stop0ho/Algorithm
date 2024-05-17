const isPrime = (n) => {
    if (n <= 1) return false;
    if (n % 2 === 0) return n === 2 ? true : false;
    const sqrt = parseInt(Math.sqrt(n))
    for (let div = 3; div <= sqrt; div += 2) {
        if (n % div === 0) return false
    }
    return true
}

function solution(nums) {
    var answer = 0;
    
    for (let i=0; i<nums.length; i++){
        for (let j=i+1; j<nums.length; j++) {
            for (let k=j+1; k<nums.length; k++) {
                if (isPrime(nums[i] + nums[j] + nums[k])) answer++
            }
        }
    }
    
    return answer;
}