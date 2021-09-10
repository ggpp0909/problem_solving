def gcd(A, B):
    while A % B != 0:
        A, B = B, A % B
    return B

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))[1:]
    tot = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tot += gcd(arr[i], arr[j])
    print(tot)
