n = int(input())

arr = [0 for i in range(n+10)]

for i in range(1, n+1):
    if i == 1 or i == 2:
        arr[i] = 1
    else:
        arr[i] = arr[i-1]+arr[i-2]

print(arr[n])