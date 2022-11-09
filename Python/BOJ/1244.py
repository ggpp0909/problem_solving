def b(n):
    global light
    if n > len(light):
        return
    for i in range(n - 1,len(light), n):
        if light[i] == 1:
            light[i] =0
        elif light[i] == 0:
            light[i] =1
    return

def g(n):
    global light
    s = n
    e = n
    while s >= 0 and e < len(light) and light[s] == light[e]:
        s -= 1
        e += 1
    s += 1
    e -= 1

    for i in range(s, e + 1):
        if light[i] == 1:
            light[i] =0
        elif light[i] == 0:
            light[i] =1
    return

M = int(input())
light = list(map(int, input().split()))
N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]
for i in arr:
    if i[0] == 1:
        b(i[1])
    else:
        g(i[1] - 1)

cnt = 0
for i in range(len(light)):
    print(light[i],end=' ')
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0
