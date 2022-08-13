import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split())) # 각 카드가 어떤 플레이어에게 가야 하는지
S = list(map(int, input().split())) # 카드를 섞는 방법

card = list(range(N))
first = card[:]
ans = -1

# 한 번 섞고 나면 i번째 위치에 있던 카드는 S[i]번째 위치로 이동
# i번째 카드를 S[i]로 이동시킨 결과를 반환하는 함수
def shuffle():
    temp = [0 for i in range(N)]
    for i in range(N):
        temp[i] = card[S[i]]
    return temp

# 카드를 분배했을때 P배열대로 분배 되었는지 확인 하는 함수
def distribute():
    temp = [0 for i in range(N)]
    for i in range(N):
        if card[i] % 3 != P[i]:
            return False
    return True

cnt = 0
while True:
    if distribute():
        print(cnt)
        break
    else:
        card = shuffle()
        if card == first:
            print(-1)
            break
        cnt += 1



