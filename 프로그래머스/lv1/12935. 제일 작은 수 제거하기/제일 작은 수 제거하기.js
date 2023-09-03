function solution(arr) {
    var answer = 0;
    arr = arr.filter((x) => x !== Math.min(...arr));
    return arr.length === 0 ? [-1] : arr;
}