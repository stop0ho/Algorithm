import datetime

def solution(m, musicinfos):
    answer = []
    d = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#':'g', 'A#':'a', 'B#':'b'}
    for key in d:
        m = m.replace(key, d[key])
    
    for musicinfo in musicinfos:
        # 시간 차이 구하기
        musicinfo = musicinfo.split(',')
        time1 = datetime.datetime.strptime(musicinfo[0], '%H:%M')
        time2 = datetime.datetime.strptime(musicinfo[1], '%H:%M')
        time_diff = time2 - time1
        time_diff = str(time_diff).split(':')
        time_diff = int(time_diff[0]) * 60 + int(time_diff[1])
        
        name = musicinfo[2]
        song = musicinfo[3]
        for key in d:
            song = song.replace(key, d[key])
        song = song * time_diff
        song = song[:time_diff]
        if m in song:
            answer.append((name, time_diff))
    
    answer.sort(key=lambda x : -x[1])
    if answer:
        return answer[0][0]
    else:
        return '(None)'

print(solution("A", ["12:00,12:01,Sing,A", "12:00,13:00,Song,A"] ))