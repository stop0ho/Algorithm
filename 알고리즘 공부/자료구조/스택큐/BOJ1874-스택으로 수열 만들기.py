n = int(input())    # 수열의 개수
a = []              # 수열 입력값 저장
s = []              # stack 초기화
res = ""            # 정답값
num = 1
p = True

for _ in range(n):
    a.append(int(input()))

for i in range(n):
    if a[i] >= num:
        while a[i] >= num:
            s.append(num)
            num += 1
            res += "+\n"
        s.pop()
        res += "-\n"
    else:
        n = s.pop()
        if n > a[i]:
            print("NO")
            p = False
            break
        else:
            res += "-\n"

if p:
    print(res)
