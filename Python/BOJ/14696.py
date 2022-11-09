n = int(input())
for k in range(n):
    #별,동,네,세 -> 4,3,2,1 인덱스로 관리
    A = [0 for i in range(5)]
    B = [0 for i in range(5)]
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)):
        A[temp[i]] += 1
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)):
        B[temp[i]] += 1

    cnt = 0
    for i in range(4, -1, -1):
        if A[i] > B[i]:
            ans = 'A'
            break
        elif A[i] < B[i]:
            ans = 'B'
            break
        else:
            cnt += 1
    if cnt == 5:
        ans = 'D'
    print(ans)