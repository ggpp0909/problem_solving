n = int(input())
tree = list(map(int, input().split()))
grow = list(map(int, input().split()))
arr = sorted(list(zip(tree, grow)), key= lambda x: x[1])

tot = 0
for i in range(len(arr)):
    tot += arr[i][0] + (i) * arr[i][1]
print(tot)