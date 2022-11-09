n = int(input())

arr = [int(input()) for i in range(n)]

temp = arr[-1]
cnt = 0
for i in range(len(arr)-2, -1, -1):
    while arr[i] >= temp:
        arr[i] -= 1
        cnt += 1
    temp = arr[i]

print(cnt)