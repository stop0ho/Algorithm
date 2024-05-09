function solution(num_list) {
    var sum = 0;
    var mul = 1;
    
    num_list.forEach(num => {sum += num; mul *= num;})
    
    return num_list.length >= 11 ? sum : mul;
}