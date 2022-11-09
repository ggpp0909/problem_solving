import sys

def find(x):
    if par[x] == x:
        return x

    par[x] = find(par[x])
    return par[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)
#
#     par[y] = x
#     power[y] += power[x]

N, M = map(int, sys.stdin.readline().rstrip().split())
power = [0]
for i in range(N):
    power.append(int(sys.stdin.readline().rstrip()))

par = list(range(N + 1))

for i in range(M):
    O, P, Q = map(int, sys.stdin.readline().rstrip().split())
    P_root = find(P)
    Q_root = find(Q)
    if O == 1: # 동맹
        par[P_root] = Q_root
        power[Q_root] += power[P_root]
        # power[P_root] = 0
    else:   # 전쟁
        if power[P_root] == power[Q_root]:
            power[P_root] = 0
            power[Q_root] = 0

        else:
            if power[P_root] > power[Q_root]:
                power[P_root] -= power[Q_root]
                # power[Q_root] = 0
                par[Q_root] = P_root
            else:
                power[Q_root] -= power[P_root]
                # power[P_root] = 0
                par[P_root] = Q_root


for i in range(1, N + 1):  # 경로압축으로 재정렬
    find(i)

remained = list(set(par[1:]))

ans = []
for i in remained:
    temp = power[i]
    if temp != 0:
        ans.append(power[i])
ans.sort()
print(len(ans))
print(*ans)




