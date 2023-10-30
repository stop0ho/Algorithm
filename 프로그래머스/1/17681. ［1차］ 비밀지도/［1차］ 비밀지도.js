function solution(n, arr1, arr2) {
    let answer = new Array(n);
    for (let i = 0; i < n; i++) {
        answer[i] = new Array(n);
    }
    
    for (var i = 0; i < n; i++) {
        var bin = arr1[i].toString(2)
        if (bin.length !== n) {
            bin = '0'.repeat(n - bin.length) + bin
        }
        for (var j = 0; j < n; j++) {
            if (bin[j] === '0') {
                answer[i][j] = ' '
            } else {
                answer[i][j] = '#'
            }
        }
    }
    
    for (var i = 0; i < n; i++) {
        var bin = arr2[i].toString(2)
        if (bin.length !== n) {
            bin = '0'.repeat(n - bin.length) + bin
        }
        for (var j = 0; j < n; j++) {
            if (bin[j] === '1') {
                answer[i][j] = '#'
            }
        }
    }
    
    for (var i=0; i<n; i++){
        answer[i] = answer[i].join('')
    }
    return answer;
}