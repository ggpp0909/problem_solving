n = int(input())
cnt = 0
for i in range(666,1001000000):
    temp = 0
    for j in str(i):
        if j == '6':
            temp += 1
        else:
            temp = 0
        
        if temp == 3:
            cnt += 1
            break
    if cnt == int(n):
        print(i)
        break