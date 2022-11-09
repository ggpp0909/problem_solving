P = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# 0 1 토글은 xor 1 연산으로 한다 (1 ^ 1 = 0, 0 ^ 1 = 1)
# 1, -1로 그냥 -1 곱하면서 해도 되는데 그냥 겉멋
def click(i, j):
    arr[i][j] ^= 1
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < 3 and 0 <= nj < 3:
            arr[ni][nj] ^= 1

def recur(cur, cnt): # 행은 cur // 3 열은 cur % 3 (겉멋 + 실용성)
    if arr == dest:
        print(cnt)
        return

    if cur == 9:
        return
        
    #이놈을 클릭할것인가 말것인가야
    recur(cur + 1, cnt)

    click(cur // 3, cur % 3)
    recur(cur + 1, cnt + 1)
    click(cur // 3, cur % 3)

for _  in range(P):
    arr = [[0, 0, 0] for i in range(3)]

    # 0 1로 바꿔주는 과정 (겉멋)
    temp = []
    for i in range(3):
        temp.append(list(input()))
    dest = [[0, 0, 0] for i in range(3)]

    for i in range(3):
        for j in range(3):
            if temp[i][j] == "*":
                dest[i][j] = 1
            else: dest[i][j] = 0

    recur(0, 0)