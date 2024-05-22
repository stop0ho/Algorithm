const solution = (N, M, data) => {
  let maxWidth = 0;
  let picCnt = 0;
  let q = [];

  const dy = [-1, 1, 0, 0];
  const dx = [0, 0, -1, 1];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (data[i][j] === 1) {
        q.push([i, j]);
        picCnt += 1;
        let tmp = 1;
        data[i][j] = 0; // 방문처리
        while (q.length !== 0) {
          let [y, x] = q.shift();
          for (let k = 0; k < 4; k++) {
            let ny = y + dy[k];
            let nx = x + dx[k];
            if (0 <= ny && ny < N && 0 <= nx && nx < M && data[ny][nx] === 1) {
              data[ny][nx] = 0; // 방문처리
              tmp += 1;
              q.push([ny, nx]);
            }
          }
        }
        maxWidth = Math.max(maxWidth, tmp);
      }
    }
  }
  console.log(picCnt);
  console.log(maxWidth);
};

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [N, M] = input[0].split(" ").map((v) => +v);
const data = [];
for (let i = 1; i < N + 1; i++) {
  data.push(input[i].split(" ").map((v) => +v));
}

solution(N, M, data);
