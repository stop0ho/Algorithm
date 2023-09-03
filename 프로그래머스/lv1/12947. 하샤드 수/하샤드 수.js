function solution(x) {
    let strX = x.toString();
    let sumX = 0
    for (let i=0; i<strX.length; i++) {
        sumX += Number(strX[i]);
    }
    return x % sumX === 0;
}