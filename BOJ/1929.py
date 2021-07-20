M, N = map(int, input().split())
visited = [False for i in range(N+10)]
lst = [] 

for i in range(2,N+1):
    if visited[i]: #배수들은 연산 X
        continue
    
    lst.append(i)    #소인수는 lst에 저장

    cnt = 2 
    while cnt*i <= N:
        visited[cnt*i] =True
        cnt += 1
    
for i in lst:
    if M <= i <= N:
        print(i, end = ' ')