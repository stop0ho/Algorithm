gold = int(input())
duck = list(map(int, input().split()))

jun = gold
jun_cnt = 0

sung = gold
sung_cnt = 0

# 준현이
for d in duck:
    jun_cnt += jun // d
    jun %= d
jun = jun + jun_cnt * duck[-1]

# 성민이
down = 0
up = 0
for i in range(1, len(duck)):
    if duck[i-1] < duck[i]:
        down = 0
        up += 1
    elif duck[i-1] > duck[i]:
        down += 1
        up = 0
    
    if down == 3:
        sung_cnt += sung // duck[i]
        sung %= duck[i]
        down = 0
    if up == 3:
        sung += sung_cnt * duck[i]
        sung_cnt = 0
        up = 0
sung = sung + sung_cnt * duck[-1]

if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")