arr= [0]
cnt = 0
cnt2 = 0
while cnt2 < 1010:
    cnt += 1
    for j in range(cnt):
        arr.append(cnt)
        cnt2 += 1

n, m = map(int, input().split())
ans = sum(arr[n:m+1])
print(ans)