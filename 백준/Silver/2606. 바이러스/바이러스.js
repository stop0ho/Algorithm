const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function solution(N, input) {
  const graph = Array.from({ length: N + 1 }, () => []);
  const visited = Array(N + 1).fill(false);
  let answer = 0;

  for (const [a, b] of input) {
    graph[a].push(b);
    graph[b].push(a);
  }

  if (graph[1].length === 0) return 0;

  const q = [1];
  visited[1] = true;

  while (q.length > 0) {
    const node = q.shift();
    answer++;

    for (const newNode of graph[node]) {
      if (!visited[newNode]) {
        visited[newNode] = true;
        q.push(newNode);
      }
    }
  }
  return answer - 1;
}

let N = -1;
let M = -1;
let count = 0;
const input = [];

rl.on("line", (line) => {
  if (N === -1) {
    N = Number(line);
    return;
  }
  if (M === -1) {
    M = Number(line);
    if (M === 0) {
      console.log(0);
      rl.close();
    }
    return;
  }

  input.push(line.split(" ").map(Number));
  count++;

  if (count === M) {
    console.log(solution(N, input));
    rl.close();
  }
});
