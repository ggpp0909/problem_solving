n = int(input())

# 에라토스 테네스 체
is_prime = [True for i in range(20000)]
is_prime[1] = False
prime = []
for i in range(2, 20000):
    if i * i > 20000:
        break

    if not is_prime[i]:
        continue

    prime.append(i)
    for j in range(i * i, 20000, i):
        is_prime[j] = False

# print(prime)
ans_arr = []
for i in range(len(prime) - 1):
    ans_arr.append(prime[i] * prime[i + 1])
# print(ans_arr)

for i in ans_arr:
    if i > n:
        print(i)
        break
