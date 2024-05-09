function solution(myString, pat) {
    myString = myString.toUpperCase()
    return myString.indexOf(pat.toUpperCase()) === -1 ? 0 : 1
}