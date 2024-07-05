function solution(fees, records) {
    let recordObject = {}
    let times = {}
    let feeArray = [];
    
    // 1. 데이터 가공
    records.forEach(element => {
        const [time, number, type] = element.split(' ')
        if (recordObject[number]) recordObject[number].push(time)
        else recordObject[number] = [time]
    })
    // 2. 만약 출차 시간이 없다면 23:59 추가
    for (const record in recordObject) {
        if (recordObject[record].length % 2 !== 0) recordObject[record].push('23:59')
    }
    // 3. 총 주차시간 계산(분 단위로 계산해야 함)
    for (const key in recordObject) {
        const record = recordObject[key]
        for (let i=0; i<record.length; i+=2) {
            const [inHour, inMinutes] = record[i].split(':').map((v) => +v)
            const [outHour, outMinutes] = record[i+1].split(':').map((v) => +v)
            const inTime = new Date(`2024/07/05 ${inHour}:${inMinutes}:00`)
            const outTime = new Date(`2024/07/05 ${outHour}:${outMinutes}:00`)
            const diffMinutes = (outTime.getTime() - inTime.getTime()) / (60 * 1000)
            if (times[key]) times[key] += diffMinutes
            else times[key] = diffMinutes
        }
    }
    // 4. 주차 요금 계산 : 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    for (const key in times) {
        const time = times[key]
        let fee = 0
        if (time <= fees[0]) fee = fees[1]
        else {
            fee = fees[1] + Math.ceil((time - fees[0]) / fees[2]) * fees[3]
        }
        feeArray.push([key, fee])
    }
    // 5. 차량번호 오름차순 정렬
    feeArray.sort((a, b) => +a[0] - +b[0])
    return feeArray.map((v) => v[1]);
}