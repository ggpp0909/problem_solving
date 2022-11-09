def gcd(A, B):
    while A % B != 0:
        A, B = B, A % B
    return B

def divisor(n):
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            real_ans.append(i)
            if i * i != n:
                real_ans.append(n//i)

n = int(input())
m = [int(input()) for i in range(n)]

arr = []
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        arr.append(abs(m[i] - m[j]))
ans = arr[0]
for i in range(1, len(arr)):
    ans = gcd(ans, arr[i])

real_ans = []
divisor(ans)
real_ans.sort()
print(*real_ans[1:])
