def boy(n):
    for i in range(n - 1, N, n):
        switch[i] ^= 1


def girl(n):
    switch[n - 1] ^= 1
    s = n - 2
    e = n
    while e < N and s >= 0 and switch[e] == switch[s]:
        switch[e] ^= 1
        switch[s] ^= 1
        e += 1
        s -= 1


N = int(input())
switch = list(map(int, input().split()))
student = int(input())

for i in range(student):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        boy(temp[1])
    else:
        girl(temp[1])


cnt = 0
for i in range(N):
    print(switch[i], end=' ')
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0



