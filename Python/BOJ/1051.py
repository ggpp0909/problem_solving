n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())

max_line = min(n,m) #가장큰 정사각형의 변

while True:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j+max_line> m or i+max_line > n: #범위 넘으면
                break
            #정사각형?
            if arr[i][j]==arr[i+max_line-1][j] and arr[i][j]==arr[i][j+max_line-1] and arr[i][j]==arr[i+max_line-1][j+max_line-1]:
                print((max_line)**2)
                exit()
            else:
                continue
            
    max_line -= 1
    if max_line == 0:
        break