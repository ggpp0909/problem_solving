def check(tot):
    global cnt
    if tot == 0:
        cnt += 1
        if cnt >= 3:
            return True
    return False

def scan():
    # 행,열체크
    for i in range(5):
        tot = 0
        tot2 = 0
        for j in range(5):
            tot += bingo[j][i]
            tot2 += bingo[i][j]
        if check(tot):
            return True
        if check(tot2):
            return True
        
    # 대각선 체크
    tot = 0
    tot2 = 0
    for i in range(5):
        tot += bingo[i][i]
        tot2 += bingo[i][4-i]
    if check(tot):
        return True
    if check(tot2):
        return True

bingo = [list(map(int, input().split())) for i in range(5)]
call = []
for i in range(5):
    call += list(map(int, input().split()))

for k in range(25):   
    cnt = 0
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == call[k]:
                bingo[i][j] = 0
                if scan():
                    print(k + 1)
                    exit()