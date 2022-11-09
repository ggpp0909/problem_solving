X = int(input())
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

temp = 0
for i in range(len(arr)):
    temp += arr[i][0] * arr[i][1]

if temp == X:
    print("YES")
else:
    print("NO")