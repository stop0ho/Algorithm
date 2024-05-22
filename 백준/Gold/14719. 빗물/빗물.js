const solution = (H, W, data) => {
  let answer = 0;
  for (let i = 1; i < W - 1; i++) {
    let lm = Math.max(...data.slice(0, i));
    let rm = Math.max(...data.slice(i + 1, W));

    let compare = Math.min(lm, rm);

    if (data[i] < compare) {
      answer += compare - data[i];
    }
  }
  console.log(answer);
};

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [H, W] = input[0].split(" ").map((v) => +v);
const data = input[1].split(" ").map((v) => +v);

solution(H, W, data);
