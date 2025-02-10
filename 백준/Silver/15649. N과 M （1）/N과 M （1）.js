const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map((v) => Number(v));
const answer = Array(10).fill(0);
const visited = Array(10).fill(false);

function dfs(k) {
  if (k == M) {
    console.log(answer.filter((_, i) => i < M).join(" "));
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      answer[k] = i;
      dfs(k + 1);
      visited[i] = false;
    }
  }
}

dfs(0);
