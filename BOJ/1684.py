import sys

def gcd(A, B):
    while A % B != 0:
        A, B = B, A % B
    return B

n = int(input())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

temp = []
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            continue
        temp.append(abs(arr[i] - arr[j]))

# print(temp)

ans = temp[0]
for i in range(1, len(temp)):
    ans = gcd(ans, temp[i])

print(ans)