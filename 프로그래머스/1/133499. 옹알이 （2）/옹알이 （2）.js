function solution(babbling) {
    const regexp1 = /^(aya|ye|woo|ma)+$/;
    const regexp2 = /(aya|ye|woo|ma)\1+/;
    
    return babbling.reduce((a, word) => (!regexp2.test(word) && regexp1.test(word) ? ++a : a), 0);
}