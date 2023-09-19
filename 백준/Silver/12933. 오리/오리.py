duck = input()
quack = 'quack'
visited = [0]*len(duck)

def check(idx):
    global cnt
    k = 0
    start = True
    for j in range(idx, len(duck)):
        if quack[k]==duck[j] and not visited[j]:
            visited[j] = 1
            if duck[j] == 'k':
                if start:
                    cnt += 1
                    start = False
                k = 0
                continue
            k += 1
cnt = 0
if len(duck)%5!=0:
    print(-1)
    exit()
else:
    for i in range(len(duck)):
        if duck[i]=='q' and not visited[i]:
            check(i)

if not all(visited) or cnt==0:
    print(-1)
else:
    print(cnt)