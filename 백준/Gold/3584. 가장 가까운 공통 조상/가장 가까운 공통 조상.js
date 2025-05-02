const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

let idx = 0;
const T = Number(input[idx++]);

for (let t = 0; t < T; t++) {
  const n = Number(input[idx++]);
  const parent = Array(n + 1).fill(0);

  for (let i = 0; i < n - 1; i++) {
    const [a, b] = input[idx++].split(" ").map(Number);
    parent[b] = a;
  }

  const [x, y] = input[idx++].split(" ").map(Number);

  const visited = Array(n + 1).fill(false);

  let cur = x;
  while (cur !== 0) {
    visited[cur] = true;
    cur = parent[cur];
  }

  let ans = y;
  while (!visited[ans]) {
    ans = parent[ans];
  }

  console.log(ans);
}
