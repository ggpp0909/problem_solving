arr =[]
for i in range(9):
    arr.append(int(input()))

tot = sum(arr)

arr.sort()

s = 0
e = len(arr)-1

while s <= e:
    if tot - (arr[s] + arr[e]) == 100:
        break
    elif tot - (arr[s] + arr[e]) > 100:
        s += 1
    else:
        e -= 1

for i in range(len(arr)):
    if i != s and i != e:
        print(arr[i])
    