const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input[0].split(" ").map((v) => Number(v));
const dolls = input[1].split(" ").map((v) => Number(v));

const solution = (N, K, dolls) => {
  let answer = Infinity;

  let start = 0;
  let count = 0;

  for (let end = 0; end < N; end++) {
    if (dolls[end] === 1) count++;

    while (count >= K) {
      answer = Math.min(answer, end - start + 1);
      if (dolls[start] === 1) count--;
      start++;
    }
  }

  return answer === Infinity ? -1 : answer;
};

console.log(solution(N, K, dolls));
