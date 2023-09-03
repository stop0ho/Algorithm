function solution(s){
    let answer = true;
    
    let countp = 0;
    let county = 0;
    
    for (let i=0; i<s.length; i++){
        if (s[i] === 'p' || s[i] === 'P') {
            countp += 1;
        }
        if (s[i] === 'y' || s[i] === 'Y') {
            county += 1;
        }
    }
    
    return countp === county;
}