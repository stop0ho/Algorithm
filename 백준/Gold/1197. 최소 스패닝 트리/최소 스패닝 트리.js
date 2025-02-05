const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

function solution(input) {
  let answer = 0;
  const n = input[0][0];
  const graph = input.slice(1);
  graph.sort((a, b) => a[2] - b[2]);
  const parent = Array(n)
    .fill(0)
    .map((_, index) => index);

  function find(u) {
    if (parent[u] === u) return u;
    return (parent[u] = find(parent[u]));
  }
  function union(u, v) {
    const root_u = find(u);
    const root_v = find(v);
    if (root_u !== root_v) parent[root_v] = root_u;
  }

  for (const [u, v, cost] of graph) {
    if (find(u) !== find(v)) {
      union(u, v);
      answer += cost;
    }
  }

  return answer;
}

console.log(solution(input));
