N, K = map(int, input().split())
prime = [True for i in range(N + 1)]
prime[1] = False
cnt = 0

for i in range(2, N + 1):
    if not prime[i]:
        continue

    for j in range(i, N + 1, i):
        if prime[j]:
            prime[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                exit()
