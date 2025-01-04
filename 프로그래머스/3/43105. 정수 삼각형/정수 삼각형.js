function createArray(n) {
  return Array.from({ length: n }, () => Array(n).fill(0));
}

function solution(triangle) {
    let triangleLength = triangle.length
    let dp = createArray(triangleLength)
    
    // 첫 줄 초기화
    dp[0][0] = triangle[0][0]
    
    for (let i=0; i<triangleLength-1; i++) {
        for (let j=0; j<triangleLength-1; j++) {
            if (dp[i+1][j] < dp[i][j] + triangle[i+1][j]) {
                dp[i+1][j] = dp[i][j] + triangle[i+1][j]
            }
            if (dp[i+1][j+1] < dp[i+1][j+1] + triangle[i+1][j+1]){
            dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]}
        }
    }
    
    return Math.max(...dp[triangleLength-1])
}