function solution(todo_list, finished) {
    let answer = []
    todo_list.forEach((todo, index) => {
        if (!finished[index]) {
            answer.push(todo)
        }
    })
    return answer
}