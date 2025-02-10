function solution(info, edges) {
    let answer = 1;
    
    let n = info.length;
    
    const tree = Array.from({length: n}, () => []);
    
    for (const [parent, child] of edges) {
        tree[parent].push(child);
    }
    
    function dfs(node, sheep, wolf, nextNodes) {
        if (info[node] === 0) sheep++;
        else wolf++;
                
        if (wolf >= sheep) return;
        
        answer = Math.max(answer, sheep);
        
        const newNextNodes = [...nextNodes];
        newNextNodes.push(...tree[node]);
        
        for (const nextNode of newNextNodes) {
            dfs(nextNode, sheep, wolf, newNextNodes.filter(n => n !== nextNode))
        }
    }
    
    dfs(0, 0, 0, []);
    return answer;
}