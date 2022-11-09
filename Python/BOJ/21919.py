def lcm(A, B):
    a, b = A, B
    while a % b != 0:
        a, b = b, a % b
    return (A * B) // b


def is_prime(n):
    flag = 0
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            flag = 1
            break
    if flag:
        return False
    return True


n = int(input())
arr = list(map(int, input().split()))

prime_arr = []
for i in arr:
    if is_prime(i):
        prime_arr.append(i)

ans = 1
for i in range(len(prime_arr)):
    ans = lcm(ans, prime_arr[i])

if ans == 1:
    print(-1)
else:
    print(ans)