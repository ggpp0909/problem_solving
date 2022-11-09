N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
arr.sort()
warehouse = [0 for i in range(1010)]
s = 0
e = len(arr) - 1
while s <= e:
    while warehouse[arr[s][0]] < arr[s][1] and warehouse[arr[e][0]] < arr[e][1]:
        for i in range(arr[s][0], arr[e][0] + 1):
            warehouse[i] += 1
    if warehouse[arr[s][0]] >= arr[s][1]:
        s += 1
    elif warehouse[arr[e][0]] >= arr[e][1]:
        e -= 1

print(sum(warehouse[arr[0][0]:arr[-1][0] + 1]))
    
