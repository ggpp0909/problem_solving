def switch(n):
    for i in range(n-1, N, n):
        if led[i] == 'N':
            led[i] = 'Y'
        elif led[i] == 'Y':
            led[i] = 'N'

led = list(input())
N = len(led)

cnt = 0
for i in range(N):
    if led[i] == 'Y':
        switch(i + 1)
        cnt += 1

print(cnt)