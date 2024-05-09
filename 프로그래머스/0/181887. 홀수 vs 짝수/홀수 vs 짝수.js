function solution(num_list) {
    let sum1 = 0;
    let sum2 = 0;
    num_list.forEach((n, i) => {
        if (i % 2 === 0) sum1 += n;
        else sum2 += n;
    })
    return sum1 > sum2 ? sum1 : sum2;
}