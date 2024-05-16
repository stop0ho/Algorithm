function solution(nums) {
    var answer = 0;
    let s = new Set(nums)
    return [...s].length < nums.length / 2 ? [...s].length : nums.length / 2;
}