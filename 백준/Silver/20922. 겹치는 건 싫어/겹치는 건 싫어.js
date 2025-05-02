const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input[0].split(" ").map((v) => Number(v));
const numbers = input[1].split(" ").map((v) => Number(v));

const solution = (N, K, numbers) => {
  let answer = 0;
  let start = 0;
  let count = new Map();

  for (let end = 0; end < N; end++) {
    const number = numbers[end];
    // 1. 숫자 개수 카운팅
    count.set(number, (count.get(number) || 0) + 1);

    // 2. 숫자가 K개를 넘어가면
    while (count.get(number) > K) {
      count.set(numbers[start], count.get(numbers[start]) - 1);
      start++;
    }

    answer = Math.max(answer, end - start + 1);
  }

  return answer;
};

console.log(solution(N, K, numbers));
