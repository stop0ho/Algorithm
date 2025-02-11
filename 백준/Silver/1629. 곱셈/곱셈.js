const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
const [A, B, C] = input.map(BigInt); // BigInt를 사용하여 큰 정수를 처리합니다.

function modularExponentiation(a, b, c) {
  if (b === 0n) return 1n;
  const half = modularExponentiation(a, b / 2n, c);
  const result = (half * half) % c;

  if (b % 2n === 0n) {
    return result;
  } else {
    return (result * a) % c;
  }
}

console.log(modularExponentiation(A, B, C).toString());