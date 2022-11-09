n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# 끝나는 시간 -> 시작시간 순으로 정렬
arr.sort(key= lambda x: (x[1], x[0]))

# print(arr)
cnt = 1
temp = arr[0][1]
for i in range(len(arr)-1):
    if temp <= arr[i+1][0]:
        cnt += 1
        temp = arr[i+1][1]

print(cnt)