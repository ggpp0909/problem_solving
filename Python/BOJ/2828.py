N, M = map(int, input().split())
num = int(input())
arr = [0 for i in range(N)]  # 게임판 너비 0으로 초기화

s = 1
e = M  # 슬라이딩윈도우
ans = 0

for i in range(num):
    pos = int(input())
    if s <= pos <= e:
        continue
    elif pos < s:
        move = s - pos
        ans += move
        s -= move
        e -= move
    else:
        move = pos - e
        ans += move
        s += move
        e += move

print(ans)
