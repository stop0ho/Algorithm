const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);

const moves = [];

function func(n, start, end, via) {
  if (n === 1) {
    moves.push(`${start} ${end}`);
    return;
  }
  // N-1개의 원반을 start에서 via로 이동
  func(n - 1, start, via, end);
  // 제일 큰 원판 start에서 end로 이동
  moves.push(`${start} ${end}`);
  // N-1개의 원판을 via에서 end로 이동
  func(n - 1, via, end, start);
}

func(n, 1, 3, 2);

console.log(moves.length);
console.log(moves.join("\n"));
