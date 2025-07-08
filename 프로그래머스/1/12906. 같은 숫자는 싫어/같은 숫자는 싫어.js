function solution(arr)
{
    // Set은 아님. 그냥 연속되는 걸 넣는 거니까
    let answer = [arr[0]];

    for (let index = 1; index < arr.length; index++) {
        if (answer[answer.length - 1] !== arr[index]) answer.push(arr[index]);
    }
    
    return answer;
}