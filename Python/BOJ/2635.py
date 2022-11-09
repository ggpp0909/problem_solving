N = int(input())

arr = []
for i in range(N + 1):
    temp = [N, i]
    idx = 0
    while True:
        a = temp[idx] - temp[idx + 1]
        if a < 0:
            break
        else:
            temp.append(a)
            idx += 1
    arr.append(temp)

max_len = 0
max_ans = 0
for i in range(len(arr)):
    temp = len(arr[i])
    if max_len < temp:
        max_len = temp
        max_ans = arr[i]

print(max_len)
print(*max_ans)