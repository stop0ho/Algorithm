function solution(participant, completion) {
    let part = {}
    let comp = {}
    
    for (const name of participant) {
        if (!(name in part)) part[name] = 1
        else part[name] += 1
    }
    for (const name of completion) {
        if (!(name in comp)) comp[name] = 1
        else comp[name] += 1
    }
    
    for (const key of Object.keys(part)) {
        if (part[key] !== comp[key]) return key
    }
}