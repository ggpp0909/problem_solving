n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if arr[0] != 1:
    print(1)
    exit()
tot = 0
idx = 0
while idx < len(arr) - 1:
    tot += arr[idx]
    if tot >= arr[idx + 1] - 1:
        idx += 1
    else: 
        print(tot + 1)
        break
else:
    print(tot + arr[-1]  + 1)