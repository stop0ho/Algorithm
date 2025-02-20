const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
const M = Number(input[2]);

const numbers = input[1]
  .split(" ")
  .map((v) => Number(v))
  .sort((a, b) => a - b);
const targets = input[3].split(" ").map((v) => Number(v));

function bs(target) {
  let start = 0;
  let end = numbers.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);

    if (numbers[mid] === target) {
      return 1;
    }
    if (numbers[mid] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return 0;
}

for (const target of targets) {
  console.log(bs(target));
}
