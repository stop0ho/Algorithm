function solution(s) {
    var answer = '';
    var numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'};
    
    var start = 0;
    var end = 1;
    while (end <= s.length) {
        temp = s.slice(start, end)
        if (!isNaN(temp)) {
            answer += temp
            start += 1
        }
        if (temp in numbers) {
            answer += numbers[temp]
            start = end
        }
        end += 1
    }
    
    
    return Number(answer);
}