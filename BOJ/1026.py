n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

tot = 0
for i in range(len(a)):
    tot += a[i] * b[i]

print(tot)