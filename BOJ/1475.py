a = input()
n = 0
arr = [0 for i in range(len(a) + 10)]

for i in a:
    arr[int(i)] += 1

temp = arr[6] + arr[9]

if temp % 2:
    arr[6] = temp // 2
    arr[9] = temp // 2 + 1
else:
    arr[6] = temp // 2
    arr[9] = temp // 2

end = max(arr)

print(end)