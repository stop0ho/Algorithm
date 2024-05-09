function solution(todo_list, finished) {
    return todo_list.filter((todo, index) => finished[index]===false)
}