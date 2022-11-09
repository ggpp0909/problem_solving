import sys

is_prime = [True for i in range(10010)]
for i in range(2, 10000):
    if i * i > 10000:
        break

    if not is_prime[i]:
        continue

    for j in range(i*i, 10010, i):
        is_prime[j] = False
prime = []
for i in range(2, len(is_prime)):
    if is_prime[i]:
        prime.append(i)

T = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for i in range(T)]

for i in arr:
    temp = 99999999999
    ans = []
    for j in prime:
        for k in prime:
            if j + k == i:
                if abs(j - k) < temp:
                    ans = [j, k]
                    temp = abs(j - k)
            elif j + k > i:
                break
    print(*ans)