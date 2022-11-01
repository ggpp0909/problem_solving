N = int(input())
arr = sorted(list(map(int, input().split())))

arr2 = [False for i in range(2000000001)]
ans = 0
for i in range(len(arr)):
    if arr2[i]:
        ans += 1
    for j in range(i + 1, len(arr)):
        arr2[arr[i] + arr[j]] = True

print(ans)
        

