const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map((v) => Number(v));
const answer = Array(10).fill(0);

function dfs(k, c) {
  if (k == M) {
    console.log(answer.slice(0, M).join(" "));
    return;
  }

  for (let i = c + 1; i <= N; i++) {
    answer[k] = i;
    dfs(k + 1, i);
  }
}

dfs(0, 0);
